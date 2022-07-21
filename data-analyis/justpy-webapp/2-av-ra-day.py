import justpy as jp
import pandas

chart_def = """
    {
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Altitude'
        },
        labels: {
            format: '{value} '
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Temperature'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} : {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Temperature',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""
# get data
data = pandas.read_csv('../reviews.csv', parse_dates=['Timestamp'])
# create new column Week
data['Week'] = data['Timestamp'].dt.strftime('%Y-%U')
# group data by average Rating of a Week
week_average = data.groupby(['Week']).mean()


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews",
                 classes="text-2 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These grapsh represent course review analaysis",
                 classes="text-3 text-center q-pt-md")

    hc = jp.HighCharts(a=wp, options=chart_def)

    hc.options.title.text = "Average Rating"
    hc.options.series[0].name = " Average Rating"
    hc.options.xAxis.title.text = "Date"
    hc.options.yAxis.title.text = "Rating"

    hc.options.xAxis.categories = list(week_average.index)
    hc.options.series[0].data = list(week_average['Rating'])
    return wp


jp.justpy(app)
