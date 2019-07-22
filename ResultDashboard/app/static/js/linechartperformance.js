option_performance = {
    textStyle: {
        fontFamily: "Consolas"
    },
    title: {
        text: 'Performance Comparison',
        subtext: 'Historical tendency',
        textStyle: {
            fontFamily: "Consolas"
        }
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: [{
        bottom: 0,
        icon:'circle',
        textStyle: {color: '#005bc2'},
        data: ['ClearLinux-Default-Runc', 'Ubuntu-Default-Runc', 'CentOS-Default-Runc','ClearLinux-Clear-Kata', 'Ubuntu-Clear-Kata', 'CentOS-Clear-Kata',],
        selected:{
            'ClearLinux-Default-Runc': true,
        'CentOS-Default-Runc': true,
        'Ubuntu-Default-Runc': true,
        'CentOS-Clear-Kata': true,
        'Ubuntu-Clear-Kata': true,
        'ClearLinux-Clear-Kata': true,
        },
        },
        {bottom: "left",
        icon:'circle',
        textStyle: {color: '#005bc2'},
        bottom:20,
        data: ['ClearLinux-Default-Kata','Ubuntu-Default-Kata','CentOS-Default-Kata','ClearLinux-Clear-Runc','Ubuntu-Clear-Runc','CentOS-Clear-Runc'],
        selected: {
        'ClearLinux-Clear-Runc': true,
        'Ubuntu-Clear-Runc': true,
        'CentOS-Clear-Runc': true,
        'ClearLinux-Default-Kata': true,
        'Ubuntu-Default-Kata': true,
        'CentOS-Default-Kata': true,

        }}
        ],
    color: ["red", '#0a549f', '#ff70c1',"skyblue", 'blue', '#00CCCC','purple','#8f8b8b','#e35132','#09e7c0','#6d16fff2','#9bb0c6'],
    toolbox: {
        show: true,
        feature: {
            mark: {show: true},
            dataView: {
                show: true,
                readOnly: true,
                buttonColor: "red",
                title: "data view",
                lang: ["Data View", "close", "fresh"],
                optionToContent: function (opt) {
                    let axisData = opt.xAxis[0].data; //坐标数据
                    let series = opt.series; //折线图数据
                    let tdHeads = '<td  style="padding: 0 10px;width:13%;">Time</td>'; //表头
                    let tdBodys = ''; //数据
                    series.forEach(function (item) {
                        //组装表头
                        tdHeads += `<td style="padding: 0 10px;width:13%;">${item.name}</td>`;
                    });

                    let table = "<div class='col-lg-12 col-md-12 col-xs-12'>" + `<table border="1" class="t_head" style="margin:0 auto;border-collapse:collapse;font-size:16px;text-align:center"><tbody><tr style="background-color:#5894d8;color:white;height:22px;">${tdHeads} </tr>`;
                    for (let i = 0, l = axisData.length; i < l; i++) {
                        for (let j = 0; j < series.length; j++) {
                            //组装表数据
                            tdBodys += `<td style="width:13%;">${series[j].data[i]}</td>`;
                        }
                        table += `<tr><td style="padding: 0 10px;width:13%;">${axisData[i]}</td>${tdBodys}</tr>`;
                        tdBodys = '';
                    }
                    table += '</tbody></table>';
                    return table;
                }
            },
            magicType: {
                show: true,
                type: ['line', 'bar'],
                title: {line: "switch to line chart", bar: "switch to bar chart"}
            },
            restore: {show: true, title: "restore"},
            saveAsImage: {show: true, title: "save"}
        }
    },
    calculable: true,
    xAxis: [
        {
            type: 'category',
            rotate:90,
            boundaryGap: false,
            data: ['01', '02', '03', '04', '05', '06', '07'],
            axisLabel: {
                show: true,
                textStyle: {
                    fontFamily: "Consolas"
                }
            }
        }
    ],
    yAxis: [
        {
            type: 'value',
            axisLabel: {
                show: true,
                textStyle: {
                    fontFamily: "Consolas"
                },
                formatter: '{value} %'
            }
        }
    ],
    series: [
        {
            name: 'ClearLinux-Default-Runc',
            type: 'line',
            smooth: true,
            lineStyle: {
                normal: {
                    color: "red",
                    width: 2
                }
            },
            areaStyle: {
                normal: {
                    color: "rgb(0,0,0,0)",
                }
            },
            itemStyle: {normal: {areaStyle: {type: 'default'}},},
            data: [20, 40, 60, 240, 260, 530, 710]
        },
        {
            name: 'Ubuntu-Default-Runc',
            type: 'line',
            smooth: true,
            lineStyle: {
                normal: {
                    color: "#0a549f",
                    width: 2
                }
            },
            areaStyle: {
                normal: {
                    color: "transparent",
                }
            },
            itemStyle: {normal: {areaStyle: {type: 'default'}}},
            data: [30, 182, 434, 791, 390, 30, 10]
        },
        {
            name: 'CentOS-Default-Runc',
            type: 'line',
            smooth: true,
            lineStyle: {
                normal: {
                    color: "#ff70c1",
                    width: 2
                }
            },
            areaStyle: {
                normal: {
                    color: "transparent",
                }
            },
            itemStyle: {normal: {areaStyle: {type: 'default'}}},
            data: []
        },
        {
            name: 'ClearLinux-Clear-Kata',
            type: 'line',
            smooth: true,
            lineStyle: {
                normal: {
                    color: "skyblue",
                    width: 2
                }
            },
            areaStyle: {
                normal: {
                    color: "transparent",
                }
            },
            itemStyle: {normal: {areaStyle: {type: 'default'}}},
            data: [23, 44, 45, 140, 160, 330, 510]
        },
        {
            name: 'Ubuntu-Clear-Kata',
            type: 'line',
            smooth: true,
            lineStyle: {
                normal: {
                    color: "blue",
                    width: 2
                }
            },
            areaStyle: {
                normal: {
                    color: "transparent",
                }
            },
            itemStyle: {normal: {areaStyle: {type: 'default'}}},
            data: [20, 232, 134, 291, 490, 20, 130]
        },
        {
            name: 'CentOS-Clear-Kata',
            type: 'line',
            smooth: true,
            lineStyle: {
                normal: {
                    color: "#00CCCC",
                    width: 2
                }
            },
            areaStyle: {
                normal: {
                    color: "transparent",
                }
            },
            itemStyle: {normal: {areaStyle: {type: 'default'}}},
            data: []
        },
        {
            name: 'ClearLinux-Default-Kata',
            type: 'line',
            smooth: true,
            lineStyle: {
                normal: {
                    color: "purple",
                    width: 2
                }
            },
            areaStyle: {
                normal: {
                    color: "transparent",
                }
            },
            itemStyle: {normal: {areaStyle: {type: 'default'}}},
            data: [120, 232, 133, 312, 224, 15, 50]
        },
        {
            name: 'Ubuntu-Default-Kata',
            type: 'line',
            smooth: true,
            lineStyle: {
                normal: {
                    color: "#8f8b8b",
                    width: 2
                }
            },
            areaStyle: {
                normal: {
                    color: "transparent",
                }
            },
            itemStyle: {normal: {areaStyle: {type: 'default'}}},
            data: [230, 532, 233, 212, 224, 295, 140]
        },
        {
            name: 'CentOS-Default-Kata',
            type: 'line',
            smooth: true,
            lineStyle: {
                normal: {
                    color: "#e35132",
                    width: 2
                }
            },
            areaStyle: {
                normal: {
                    color: "transparent",
                }
            },
            itemStyle: {normal: {areaStyle: {type: 'default'}}},
            data: []
        },
        {
            name: 'ClearLinux-Clear-Runc',
            type: 'line',
            smooth: true,
            lineStyle: {
                normal: {
                    color: "#09e7c0",
                    width: 2
                }
            },
            areaStyle: {
                normal: {
                    color: "transparent",
                }
            },
            itemStyle: {normal: {areaStyle: {type: 'default'}}},
            data: [32, 181, 123, 321, 456, 654, 610]
        },
        {
            name: 'Ubuntu-Clear-Runc',
            type: 'line',
            smooth: true,
            lineStyle: {
                normal: {
                    color: "#6d16fff2",
                    width: 2
                }
            },
            areaStyle: {
                normal: {
                    color: "transparent",
                }
            },
            itemStyle: {normal: {areaStyle: {type: 'default'}}},
            data: [330, 232, 344, 921, 490, 150, 126]
        },
        {
            name: 'CentOS-Clear-Runc',
            type: 'line',
            smooth: true,
            lineStyle: {
                normal: {
                    color: "#9bb0c6",
                    width: 2
                }
            },
            areaStyle: {
                normal: {
                    color: "transparent",
                }
            },
            itemStyle: {normal: {areaStyle: {type: 'default'}}},
            data: []
        },
    ]
};


var lineChart_performance = echarts.init(document.getElementById('lineChart_performance'));
lineChart_performance.setOption(option_performance);
$(window).resize(function () {
    lineChart_performance.resize();
});
