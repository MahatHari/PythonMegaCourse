import pandas
import justpy as jp


# chart
def_chart = """ {
    chart: {
        type: 'areaspline'
    },
    title: {
        text: 'Average fruit consumption during one week'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor:'#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Fruit units'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""

# load data

data = pandas.read_csv('../reviews.csv', parse_dates=['Timestamp'])

data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average_bycourse = data.groupby(['Month', 'Course Name'])[
    'Rating'].count().unstack()

# web app


def app():
    wp = jp.QuasarPage()

    h1 = jp.QDiv(a=wp, text="Title for Page",
                 classes="text-h2 text-center p-pt-md")
    h2 = jp.QDiv(a=wp,  text="Sub title",
                 classes="text-h3 text-center p-pt-md ")

    # add chart
    hc = jp.HighCharts(a=wp, options=def_chart)

    hc.options.xAxis.categories = list(month_average_bycourse.index)
    hc_data = [{"name": v1, "data": [v2 for v2 in month_average_bycourse[v1]]}
               for v1 in month_average_bycourse.columns]
    hc.options.series = hc_data

    return wp


jp.justpy(app)
