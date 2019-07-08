    // 基于准备好的dom，初始化echarts实例
    var myChartPie = echarts.init(document.getElementById('OverallPie'));
    optionPie = {
    textStyle: {
       fontFamily:"Consolas"
    },
    title : {
        text: 'Test Result Situation',
        subtext: '',
        x:'center',
        textStyle: {
            fontFamily:"Consolas"
        }
    },
    tooltip : {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    legend: {
        orient : 'vertical',
        x : 'left',
        data:['Fail',"Pass"]
    },
    toolbox: {
        show : true,
        feature : {
            mark : {show: true},
            magicType : {
                show: true,
                type: ['pie', 'funnel'],
                option: {
                    funnel: {
                        x: '25%',
                        width: '50%',
                        funnelAlign: 'left',
                        max: 1548
                    }
                }
            },
            restore : {show: true,title:"restore"},
            saveAsImage : {show: true,title:"save"}
        }
    },
    calculable : true,
    series : [
        {
            name:'MicroService',
            type:'pie',
            radius : '55%',
            center: ['50%', '60%'],
            data:[
                {value:335, name:'Fail'},
                {value:310, name:'Pass'},
            ]
        }
    ],
    color:["red","#005bc2"]
};
    var labelTop = {
    normal : {
        label : {
            show : true,
            position : 'center',
            formatter : '{b}',
            textStyle: {
                baseline : 'bottom'
            }
        },
        labelLine : {
            show : false
        }
    }
};
var labelFromatter = {
    normal : {
        label : {
            formatter : function (params){
                return 100 - params.value + '%'
            },
            textStyle: {
                baseline : 'top'
            }
        }
    },
}
var labelBottom = {
    normal : {
        color: '#ccc',
        label : {
            show : true,
            position : 'center'
        },
        labelLine : {
            show : false
        }
    },
    emphasis: {
        color: 'rgba(0,0,0,0)'
    }
};
myChartPie.setOption(optionPie);
$(window).resize(function () {
  myChartPie.resize()
});

