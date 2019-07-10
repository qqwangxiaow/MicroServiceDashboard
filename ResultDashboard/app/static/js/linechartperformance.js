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
    legend: {
        bottom: "left",
        data: ['ClearLinux-Default', 'Ubuntu-Default', 'CentOS-Default','ClearLinux-Clear', 'Ubuntu-Clear', 'CentOS-Clear'],
    },
    color: ["#005bc2", 'red', '#00b5fb',"#025e79", '#efa3a3', '#bdc7fb'],
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
            name: 'ClearLinux-Default',
            type: 'line',
            smooth: true,
            lineStyle: {
                normal: {
                    color: "#005bc2",
                    width: 2
                }
            },
            areaStyle: {
                normal: {
                    color: "#005bc2",
                }
            },
            itemStyle: {normal: {areaStyle: {type: 'default'}}},
            data: [20, 40, 60, 240, 260, 530, 710]
        },
        {
            name: 'Ubuntu-Default',
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
                    color: "red",
                }
            },
            itemStyle: {normal: {areaStyle: {type: 'default'}}},
            data: [30, 182, 434, 791, 390, 30, 10]
        },
        {
            name: 'CentOS-Default',
            type: 'line',
            smooth: true,
            lineStyle: {
                normal: {
                    color: "#00b5fb",
                    width: 2
                }
            },
            areaStyle: {
                normal: {
                    color: "#00b5fb",
                }
            },
            itemStyle: {normal: {areaStyle: {type: 'default'}}},
            data: [520, 532, 601, 234, 120, 90, 20]
        },
        {
            name: 'ClearLinux-Clear',
            type: 'line',
            smooth: true,
            lineStyle: {
                normal: {
                    color: "#025e79",
                    width: 2
                }
            },
            areaStyle: {
                normal: {
                    color: "#025e79"
                }
            },
            itemStyle: {normal: {areaStyle: {type: 'default'}}},
            data: [23, 44, 45, 140, 160, 330, 510]
        },
        {
            name: 'Ubuntu-Clear',
            type: 'line',
            smooth: true,
            lineStyle: {
                normal: {
                    color: "#efa3a3",
                    width: 2
                }
            },
            areaStyle: {
                normal: {
                    color: "#efa3a3",
                }
            },
            itemStyle: {normal: {areaStyle: {type: 'default'}}},
            data: [20, 232, 134, 291, 490, 20, 130]
        },
        {
            name: 'CentOS-Clear',
            type: 'line',
            smooth: true,
            lineStyle: {
                normal: {
                    color: "#bdc7fb",
                    width: 2
                }
            },
            areaStyle: {
                normal: {
                    color: "#bdc7fb",
                }
            },
            itemStyle: {normal: {areaStyle: {type: 'default'}}},
            data: [220, 432, 333, 212, 124, 95, 40]
        }
    ]
};


var lineChart_performance = echarts.init(document.getElementById('lineChart_performance'));
lineChart_performance.setOption(option_performance);
$(window).resize(function () {
    lineChart_performance.resize();
});
