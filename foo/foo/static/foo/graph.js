var self_inv = 50;
var lol = 0;


// function change() {
//     document.getElementById("myButton1").value="Close Curtain";
//     if (lol == 0)
//         lol = 1;
//     else if (lol == 1)
//         lol = 0;
//     draw();
// }

// function draw() {
//         // Graph scripts here
//     var graphData = [[{
//         // Visits
//         data: [ [6, 1300], [7, 1600], [8, 1900], [9, 2100], [10, 2500], [11, 2200], [12, 2000], [13, 1950], [14, 1900], [15, 2000] ],
//         color: 'turquoise'
//     }], [{
//         // Returning Visits
//         data: [ [6, 1300 + self_inv], [7, 1600 + self_inv], [8, 1900 + self_inv], [9, 2100 + self_inv], [10, 2500 + self_inv], [11, 2200 + self_inv], [12, 2000 + self_inv], [13, 1950 + self_inv], [14, 1900 + self_inv], [15, 2000 + self_inv] ],
//         color: 'purple',
//         points: { radius: 4 }
//     }]
//     ];

//     $.plot($('#graph-lines'), graphData[lol], {
//         series: {
//             points: {
//                 show: true,
//                 radius: 5
//             },
//             lines: {
//                 show: true
//             },
//             shadowSize: 0
//         },
//         grid: {
//             color: '#646464',
//             borderColor: 'transparent',
//             borderWidth: 20,
//             hoverable: true
//         },
//         xaxis: {
//             tickColor: 'transparent',
//             tickDecimals: 2
//         },
//         yaxis: {
//             tickSize: 1000
//         }
//     });

//     $.plot($('#graph-lines2'), graphData[lol], {
//         series: {
//             points: {
//                 show: true,
//                 radius: 5
//             },
//             lines: {
//                 show: true
//             },
//             shadowSize: 0
//         },
//         grid: {
//             color: '#646464',
//             borderColor: 'transparent',
//             borderWidth: 20,
//             hoverable: true
//         },
//         xaxis: {
//             tickColor: 'transparent',
//             tickDecimals: 2
//         },
//         yaxis: {
//             tickSize: 1000
//         }
//     });

//     $.plot($('#graph-lines3'), graphData[lol], {
//         series: {
//             points: {
//                 show: true,
//                 radius: 5
//             },
//             lines: {
//                 show: true
//             },
//             shadowSize: 0
//         },
//         grid: {
//             color: '#646464',
//             borderColor: 'transparent',
//             borderWidth: 20,
//             hoverable: true
//         },
//         xaxis: {
//             tickColor: 'transparent',
//             tickDecimals: 2
//         },
//         yaxis: {
//             tickSize: 1000
//         }
//     });

//     $.plot($('#graph-lines4'), graphData[lol], {
//         series: {
//             points: {
//                 show: true,
//                 radius: 5
//             },
//             lines: {
//                 show: true
//             },
//             shadowSize: 0
//         },
//         grid: {
//             color: '#646464',
//             borderColor: 'transparent',
//             borderWidth: 20,
//             hoverable: true
//         },
//         xaxis: {
//             tickColor: 'transparent',
//             tickDecimals: 2
//         },
//         yaxis: {
//             tickSize: 1000
//         }
//     });

//     $.plot($('#graph-lines5'), graphData[lol], {
//         series: {
//             points: {
//                 show: true,
//                 radius: 5
//             },
//             lines: {
//                 show: true
//             },
//             shadowSize: 0
//         },
//         grid: {
//             color: '#646464',
//             borderColor: 'transparent',
//             borderWidth: 20,
//             hoverable: true
//         },
//         xaxis: {
//             tickColor: 'transparent',
//             tickDecimals: 2
//         },
//         yaxis: {
//             tickSize: 1000
//         }
//     });

//     $.plot($('#graph-lines6'), graphData[lol], {
//         series: {
//             points: {
//                 show: true,
//                 radius: 5
//             },
//             lines: {
//                 show: true
//             },
//             shadowSize: 0
//         },
//         grid: {
//             color: '#646464',
//             borderColor: 'transparent',
//             borderWidth: 20,
//             hoverable: true
//         },
//         xaxis: {
//             tickColor: 'transparent',
//             tickDecimals: 2
//         },
//         yaxis: {
//             tickSize: 1000
//         }
//     });

//     $.plot($('#graph-lines7'), graphData[lol], {
//         series: {
//             points: {
//                 show: true,
//                 radius: 5
//             },
//             lines: {
//                 show: true
//             },
//             shadowSize: 0
//         },
//         grid: {
//             color: '#646464',
//             borderColor: 'transparent',
//             borderWidth: 20,
//             hoverable: true
//         },
//         xaxis: {
//             tickColor: 'transparent',
//             tickDecimals: 2
//         },
//         yaxis: {
//             tickSize: 1000
//         }
//     });
// }


// $(document).ready(function () {
//     draw();
// });