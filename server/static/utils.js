function get_history_volumes() {
    $(document).ready(function () {
        var data = {
            code: $("#code").val(),
            start_date: String($("#start_date").val()),
            end_date: String($("#end_date").val())
        };
        console.log(data);
        $.ajax({
            url: "/history_volumes",
            data: data,
            success: render
        });
    });

    function render(data) {
        console.log(data);
        if (!data) return 0;
        data = JSON.parse(data);
        var myChart = echarts.init(document.getElementById('main'));
        option = {
            tooltip: {},
            visualMap: {
                max: data.max,
                inRange: {
                    color: ["#C0392B","#E74C3C","#9B59B6","#8E44AD","#2980B9","#3498DB","#1ABC9C","#16A085","#27AE60",
                        "#2ECC71","#F1C40F","#F39C12","#E67E22","#D35400","#95A5A6","#7F8C8D"]
                }
            },
            xAxis3D: {
                type: 'category',
            },
            yAxis3D: {
                type: 'category'
            },
            zAxis3D: {
                type: 'value'
            },
            grid3D: {
                // boxWidth: 200,
                // boxDepth: 80,
                viewControl: {
                    // projection: 'orthographic'
                },
                light: {
                    main: {
                        intensity: 1.2,
                        shadow: true
                    },
                    ambient: {
                        intensity: 0.3
                    }
                }
            },
            series: [{
                type: 'bar3D',
                data: data.data.map(function (item) {
                    return {
                        value: [item[0], item[1], item[2]],
                    }
                }),
                shading: 'lambert',

                label: {
                    fontSize: 16,
                    borderWidth: 1
                },

                emphasis: {
                    label: {
                        fontSize: 20,
                        color: '#900'
                    },
                    itemStyle: {
                        color: '#900'
                    }
                }
            }]
        }
        myChart.setOption(option);
    }


}

function init() {
    $(document).ready(function () {
        $('#start_date').val(new Date().toISOString().substring(0, 10));
        $('#end_date').val(new Date().toISOString().substring(0, 10));
        // $(".AttrDate").datepicker();
        $(".AttrDate").on("change",function(){
            get_history_volumes();
        });
        $(".Attr").on("change",function(){
            get_history_volumes();
        });
        $.ajax({
            url: "/code_list",
            success: init_code_list
        });
    });
}

function init_code_list(code_list) {
    $.each(code_list, function (key, value) {
        $('#code')
            .append($("<option></option>")
                .attr("value", key)
                .text(value));    //测试
    });
}