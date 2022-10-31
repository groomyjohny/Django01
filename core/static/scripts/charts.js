// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
//google.charts.setOnLoadCallback(drawChart);

// Callback that creates and populates a data table,
// instantiates the chart, passes in the data and
// draws it.
function drawChart(rows)
{
    // Create the data table.
    var data = new google.visualization.DataTable();
    data.addColumn('date', 'Дата и время');
    data.addColumn('number', 'Время (нс)');
    data.addRows(rows);

    // Set chart options
    var options = {'title':'Время процессора',
                   'width':1000,
                   'height':800};

    // Instantiate and draw our chart, passing in some options.
    var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
        chart.draw(data, options);
}

function dateToPython(d)
{
    return d.toISOString();
}

async function handleForm(e)
{
    let form = document.getElementById("input-form-2");
    let data = new FormData(form);

    let procName = data.get("procName");
    let dateBegin = new Date(data.get("dateBegin"));
    let dateEnd = new Date(data.get("dateEnd"));
    let samplingPoints = parseInt(data.get("samplingPoints"));

    fetch('get_data', {
        method: "POST",
        body: JSON.stringify({
            procName: procName,
            dateRange: [dateToPython(dateBegin), dateToPython(dateEnd)],
            samplingPoints: samplingPoints,
        })
    }).then(async (response) =>
        {
            let chartData = await response.json();
            for (let i = 0; i < chartData.length; ++i)
                chartData[i][0] = new Date(chartData[i][0]);

            drawChart(chartData);
        }
    );
}