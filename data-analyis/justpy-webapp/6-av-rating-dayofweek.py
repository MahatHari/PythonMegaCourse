import pandas
import justpy as jp
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

# load data

data = pandas.read_csv('../reviews.csv', parse_dates=['Timestamp'])

data['Day'] = data['Timestamp'].dt.strftime('%A')  # %A gives WeekDay
data['DayNum'] = data['Timestamp'].dt.strftime('%w')  # %w gives Day Number

weekDay_average = data.groupby(['Day', 'DayNum']).mean()

# sorting
weekDay_average = weekDay_average.sort_values('DayNum')


# web app


def app():
    wp = jp.QuasarPage()

    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews",
                 classes="text-h2 text-center p-pt-md")
    h2 = jp.QDiv(a=wp,  text="Aggregated Average Ratings by Day of Week",
                 classes="text-h3 text-center p-pt-md ")

    # add chart
    hc = jp.HighCharts(a=wp, options=def_chart)

    hc.options.title.text = "Analysis of Course Reviews"
    hc.options.series[0].name = " Aggregated Average Ratings by Day of Week"
    hc.options.xAxis.title.text = "Day"
    hc.options.yAxis.title.text = "Rating"

    # supply data to chart
    hc.options.xAxis.categories = list(
        weekDay_average.index.get_level_values(0))

    hc.options.series[0].data = list(weekDay_average['Rating'])

    return wp


jp.justpy(app)
