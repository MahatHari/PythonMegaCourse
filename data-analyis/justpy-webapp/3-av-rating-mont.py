import justpy as jp
import pandas
from requests import options


def_chart = """{
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

# group data by month
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average = data.groupby(['Month']).mean()


def app():
    wp = jp.QuasarPage()  # wp => webpage
    h2 = jp.QDiv(a=wp, text="Average Rating by Month",
                 classes="text-h2 q-pa-md text-center")
    h3 = jp.QDiv(a=wp, text="Practice", classes="text-h3 q-pa-md text-center")

    hc = jp.HighCharts(a=wp, options=def_chart)

    # chart lables
    hc.options.title.text = "Average Rating"
    hc.options.series[0].name = " Average Rating"
    hc.options.xAxis.title.text = "Date"
    hc.options.yAxis.title.text = "Rating"

    # passing data to chart
    hc.options.xAxis.categories = list(month_average.index)
    hc.options.series[0].data = list(month_average['Rating'])

    return wp


# call the app
jp.justpy(app)
