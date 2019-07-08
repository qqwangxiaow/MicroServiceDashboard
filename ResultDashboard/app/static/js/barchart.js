var myChartBar = echarts.init(document.getElementById('OverallBar'));
var posList = [
    'left', 'right', 'top', 'bottom',
    'inside',
    'insideTop', 'insideLeft', 'insideRight', 'insideBottom',
    'insideTopLeft', 'insideTopRight', 'insideBottomLeft', 'insideBottomRight'
];

myChartBar.configParameters = {
    rotate: {
        min: -90,
        max: 90
    },
    align: {
        options: {
            left: 'left',
            center: 'center',
            right: 'right'
        }
    },
    verticalAlign: {
        options: {
            top: 'top',
            middle: 'middle',
            bottom: 'bottom'
        }
    },
    position: {
        options: echarts.util.reduce(posList, function (map, pos) {
            map[pos] = pos;
            return map;
        }, {})
    },
    distance: {
        min: 0,
        max: 100
    }
};

myChartBar.config = {
    rotate: 90,
    align: 'left',
    verticalAlign: 'middle',
    position: 'insideBottom',
    distance: 15,
    onChange: function () {
        var labelOption = {
            normal: {
                rotate: myChartBar.config.rotate,
                align: mychartbar.config.align,
                verticalAlign: mychartbar.config.verticalAlign,
                position: mychartbar.config.position,
                distance: mychartbar.config.distance
            }
        };
        myChart.setOption({
            series: [{
                label: labelOption
            }, {
                label: labelOption
            }, {
                label: labelOption
            }, {
                label: labelOption
            }]
        });
    }
};


var labelOption = {
    normal: {
        color: '#fff',
        show: true,
        position: myChartBar.config.position,
        distance: myChartBar.config.distance,
        align: myChartBar.config.align,
        verticalAlign: myChartBar.config.verticalAlign,
//        rotate: myChartBar.config.rotate,
        formatter: '{c}',
        fontSize: 14,
//        rich: {
//            name: {
//                textBorderColor: '#fff'
//            }
//        }
    }
};

option = {
    textStyle: {
       fontFamily:"Consolas"
    },
    title : {
        text: 'Performance Situation',
        textStyle: {
            fontFamily:"Consolas"
        }
    },
    color: ["#005bc2", 'red', '#9cd8f8'],
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow'
        }
    },
    legend: {
        data: ['ClearLinux', 'Ubuntu', 'CentOS']
    },
    toolbox: {
        show: true,
        orient: 'vertical',
        left: 'right',
        top: 'center',
        feature: {
            mark: {show: true},
            dataView: {show: true, readOnly: true,title:"Data View",buttonColor:"red",lang:["Data View","close","fresh"],optionToContent:function (opt) {
            let axisData = opt.xAxis[0].data; //坐标数据
            let series = opt.series; //折线图数据
            let tdHeads = '<td  style="padding: 0 10px;width:20%;">MicroService</td>'; //表头
            let tdBodys = ''; //数据
            series.forEach(function (item) {
                //组装表头
                tdHeads += `<td style="padding: 0 10px;width:20%;">${item.name}</td>`;
            });
            let table = `<table border="1" class="t_head" style="margin:0 auto;border-collapse:collapse;font-size:16px;text-align:center"><tbody><tr style="background-color:#5894d8;color:white;height:20px;">${tdHeads} </tr>`;
            for (let i = 0, l = axisData.length; i < l; i++) {
                for (let j = 0; j < series.length; j++) {
                    //组装表数据
                    tdBodys += `<td style="width:20%;">${ series[j].data[i]}</td>`;
                }
                table += `<tr><td style="padding: 0 10px;width:20%;">${axisData[i]}</td>${tdBodys}</tr>`;
                tdBodys = '';
            }
            table += '</tbody></table>';
            return table;
        }},
            restore: {show: true,title:"restore"},
            saveAsImage: {show: true,title:"save"}
        }
    },
    calculable: true,
    xAxis: [
        {
            type: 'category',
            axisTick: {show: false},
            data: ['Python', 'Java', 'Nginx', 'Ruby', 'Jenkins'],
            axisLabel: {
                                show: true,
                                textStyle: {
                                    fontFamily:"Consolas"
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
                                    fontFamily:"Consolas"
                                }
                            }
        }
    ],
    series: [
        {
            name: 'ClearLinux',
            type: 'bar',
            barGap: 0,
            label: labelOption,
            data: [320, 332, 301, 334, 390]
        },
        {
            name: 'Ubuntu',
            type: 'bar',
            label: labelOption,
            data: [220, 182, 191, 234, 290]
        },
        {
            name: 'CentOS',
            type: 'bar',
            label: labelOption,
            data: [150, 232, 201, 154, 190]
        },
    ]
};
myChartBar.setOption(option);

var myChartBar2 = echarts.init(document.getElementById('OverallBar2'));
optionBar2 = {
    textStyle: {
       fontFamily:"Consolas"
    },
    title : {
        text: 'Failed Test Situation',
        textStyle: {
            fontFamily:"Consolas"
        }
    },
    tooltip : {
        trigger: 'axis',
        axisPointer : {            // 坐标轴指示器，坐标轴触发有效
            type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        },
        formatter: function (params){
            return params[0].name + '<br/>'
                   + params[0].seriesName + ' : ' + params[0].value + '<br/>'
                   + params[1].seriesName + ' : ' + (params[1].value + params[0].value);
        }
    },
    legend: {
        selectedMode:false,
        data:['Failed', 'Passed']
    },
    toolbox: {
        show : true,
        feature : {
            mark : {show: true},
            dataView : {show: true, readOnly: true,buttonColor:"red",title:"Data View",lang:["Data View","close","fresh"],optionToContent:function (opt) {
            let axisData = opt.xAxis[0].data; //坐标数据
            let series = opt.series; //折线图数据
            let tdHeads = '<td  style="padding: 0 10px;width:20%;">MicroService</td>'; //表头
            let tdBodys = ''; //数据
             //组装表头
            tdHeads += '<td style="padding: 0 10px">Total</td>'+'<td style="padding: 0 10px">Failed</td>'+'<td style="padding: 0 10px">Passed</td>';

            let table = `<table border="1" class="t_head" style="margin:0 auto;border-collapse:collapse;font-size:16px;text-align:center"><tbody><tr style="background-color:#5894d8;color:white;height:22px;">${tdHeads} </tr>`;
            for (let i = 0; i < 6; i++) {
                for  (let j = 0; j < 3; j++){
                    //组装表数据
                    if(j==2){
                        tdBodys += `<td style="width:20%;">${ series[0].data[i]-series[1].data[i]}</td>`;
                        continue
                    }
                    console.log(series[j].data[i])
                    tdBodys += `<td style="width:20%;">${ series[j].data[i]}</td>`;
                }
                table += `<tr><td style="padding: 0 10px;width:20%;">${axisData[i]}</td>${tdBodys}</tr>`;
                tdBodys = '';
            }
            table += '</tbody></table>';
            return table;
        }},
            restore : {show: true,title:"restore"},
            saveAsImage : {show: true,title:"save"}
        }
    },
    calculable : true,
    xAxis : [
        {
            type : 'category',
            data : ['Python','JAVA','Redis','MariaDB','Ruby','MongoDB'],
            axisLabel: {
                                show: true,
                                textStyle: {
                                    fontFamily:"Consolas"
                                }
                            }
        }
    ],
    yAxis : [
        {
            type : 'value',
            boundaryGap: [0, 0.1],
            axisLabel: {
                                show: true,
                                textStyle: {
                                    fontFamily:"Consolas"
                                }
                            }
        }
    ],
    series : [
        {
            name:'Passed',
            type:'bar',
            stack: 'one',
            barCategoryGap: '50%',
            itemStyle: {
                normal: {
                    color: '#005bc2',
                    barBorderColor: '#005bc2',
                    barBorderWidth: 0,
                    barBorderRadius:0,
                    label : {
                        show: true, position: 'insideTop'
                    }
                }
            },
            data:[360, 500, 800, 790, 400, 900]
        },
        {
            name:'Total',
            type:'bar',
            stack: 'one',
            itemStyle: {
                normal: {
                    color: '#f00',
                    barBorderColor: '#005bc2',
                    barBorderWidth: 0,
                    barBorderRadius:0,
                    label : {
                        show: true,
                        position: 'insideTop',
                        formatter: function (params) {
                            for (var i = 0, l = optionBar2.xAxis[0].data.length; i < l; i++) {
                                if (optionBar2.xAxis[0].data[i] == params.name) {
                                    return  params.value;
                                }
                            }
                        },
                        textStyle: {
                            color: '#fff',
                            fontStyle: 'Consolas'
                        }
                    }
                }
            },
            data:[120, 90, 75, 79,83, 87]
        },
        {
            name:'Failed',
            type:'bar',
            stack: 'one',
            itemStyle: {
                normal: {
                    color: '#f00',
                    barBorderColor: '#005bc2',
                    barBorderWidth: 0,
                    barBorderRadius:0,
                    label : {
                        show: true,
                        position: 'insideBottom',
                        formatter: function (params) {
                            for (var i = 0, l = optionBar2.xAxis[0].data.length; i < l; i++) {
                                if (optionBar2.xAxis[0].data[i] == params.name) {
                                    return  params.value;
                                }
                            }
                        },
                        textStyle: {
                            color: '#005bc2',
                            fontStyle: 'Consolas'
                        }
                    }
                }
            },
        }
    ]
};

myChartBar2.setOption(optionBar2);
 $(window).resize(function () {
     myChartBar.resize();
     myChartBar2.resize();
 });