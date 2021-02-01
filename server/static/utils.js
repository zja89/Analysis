function get_history_volumes() {
    $(document).ready( function() {
        var data = {star_date:String($("#start_date").val()),end_date:String($("#end_date").val())};
        console.log(data);
        $.ajax({
            url: "/history_volumes",
            data: data,
            success: render
        });
    });
    function render(data) {
        console.log(data);
        data = JSON.parse(data);
        var myChart = echarts.init(document.getElementById('main'));
        var option = {
            title: {
                text: '第一个 ECharts 实例'
            },
            tooltip: {},
            legend: {
                data:['volume']
            },
            xAxis: {
                data: data.prices
            },
            yAxis: {},
            series: [{
                name: 'volume',
                type: 'bar',
                data: data.volumes
            }]
        };
        myChart.setOption(option);
    }


}

function init() {
    $(document).ready( function() {
        $('#start_date').val(new Date().toISOString().substring(0, 10));
        $('#end_date').val(new Date().toISOString().substring(0, 10));
    });
}