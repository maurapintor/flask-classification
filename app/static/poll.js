/**
 * Simple long polling client based on JQuery
 * https://github.com/sigilioso/long_polling_example/blob/master/static/poll.js
 */

/**
 * Request an update to the server and once it has answered, then update
 * the content and request again.
 * The server is supposed to response when a change has been made on data.
 */
function update(jobId) {
    $.ajax({
        url: `/classifications/${jobId}`,
        success: function (data) {
            console.log(data)
            if (data['task_status'] === "finished") {
                $('#waitText').text("");
                makeGraph(data['data']);
            } else {
                $('#waitText').text("please wait...");
                setTimeout(function () {
                    update(jobId);
                }, 1000);
            }

        }
    });
}


$(document).ready(function () {
    var scripts = document.getElementById('polling');
    var jobID = scripts.getAttribute('jobid');
    update(jobID);
});

function makeGraph(results) {
    var ctx = document.getElementById("classificationOutput").getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'horizontalBar',
        data: {
            labels: [results[0][0], results[1][0], results[2][0], results[3][0], results[4][0]],
            datasets: [{
                label: 'Output scores',
                data: [results[0][1], results[1][1], results[2][1], results[3][1], results[4][1]],
                backgroundColor: [
                    'rgba(54, 162, 23, 0.8)',
                    'rgba(255,0,53, 0.8)',
                    'rgba(255, 206, 86, 0.8)',
                    'rgb(83,117,221, 0.8)',
                    'rgb(186,93,225, 0.8)',
                ],
                borderColor: [
                    'rgba(54, 162, 23)',
                    'rgba(255,0,53)',
                    'rgba(255, 206, 86)',
                    'rgb(83,117,221)',
                    'rgb(186,93,225)',
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}