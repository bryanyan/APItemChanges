function showResult(str, count) {
    if (str.length==0) { 
      document.getElementById("livesearch" + count).innerHTML="";
      document.getElementById("livesearch" + count).style.border="0px";
      return;
    }
    if (window.XMLHttpRequest) {
      // code for IE7+, Firefox, Chrome, Opera, Safari
      xmlhttp=new XMLHttpRequest();
    } else {  // code for IE6, IE5
      xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange=function() {
      if (xmlhttp.readyState==4 && xmlhttp.status==200) {
        document.getElementById("livesearch" + count).innerHTML=xmlhttp.responseText;
        document.getElementById("livesearch" + count).style.border="1px solid #A5ACB2";
      }
    }
    xmlhttp.open("GET","livesearch.php?q="+str+"&c="+count,true);
    xmlhttp.send();
}

var count = 1;

function createPanel() {
    $('.hero').append(
        $('<div class="col-md-5 col-md-offset-1">').append(
            $('<div class="panel panel-info" id="options' + count + '">').append(
                $('<div class="panel-heading">').append(
                    $('<button type="button" class="close" data-target="#options' + count + '" data-dismiss="alert">').append(
                        $('<span aria-hidden="true">').html("&times;")
                    ),
                    "Panel " + count
                ),
                $('<div class="panel-body">').append(
                    $('<div class="row">').append(
                        $('<div class="col-md-4">').append(
                            $('<select class="form-control" id="tier' + count + '">').append(
                                $('<option value="bronze">').html('Bronze'),
                                $('<option value="bronze">').html('Silver'),
                                $('<option value="bronze">').html('Gold'),
                                $('<option value="bronze">').html('Platinum'),
                                $('<option value="bronze">').html('Diamond'),
                                $('<option value="bronze">').html('Master'),
                                $('<option value="bronze">').html('Challenger')
                            )
                        ),
                        $('<div class="col-md-4">').append(
                            $('<select class="form-control" id="region' + count + '">').append(
                                $('<option value="BR">').html('BR'),
                                $('<option value="EUNE">').html('EUNE'),
                                $('<option value="EUW">').html('EUW'),
                                $('<option value="KR">').html('KR'),
                                $('<option value="LAN">').html('LAN'),
                                $('<option value="LAS">').html('LAS'),
                                $('<option value="NA">').html('NA'),
                                $('<option value="OCE">').html('OCE'),
                                $('<option value="RU">').html('RU'),
                                $('<option value="TR">').html('TR')
                            )
                        ),
                        $('<div class="col-md-4">').append(
                            $('<button class="btn btn-success" onclick="lineGraph("#graph' + count + ' svg", getChampData(inputarea' + count + '.value));">').html('Update Info')
                        )
                    ),
                    $('<div class="row">').append(
                        $('<div class="col-md-12">').append(
                            $('<div id="graph' + count + '">').append(
                                $('<svg>')
                            )
                        )
                    )
                ),
                $('<div class="panel-footer">').append(
                    $('<div class="container">').append(
                        $('<div class="col-md-6">').append(
                            $('<input class="inputarea" id="inputarea' + count + '" type="text" size="70" style="color:#000000;" onkeyup="showResult(this.value, ' + count + ')">'),
                            $('<div id="livesearch' + count + '">')
                        ),
                        $('<div class="col-md-6">').append(
                            $('<button class="btn btn-default">').html("Add Champ")
                        )
                    )
                )
            )
        )
    );
    count += 1;
}

function selectRecommendation(html, id) {
    var search = "livesearch" + id;
    document.getElementById('inputarea' + id).value = html.innerHTML;
    $('#' + search).empty();
}

function lineGraph(id, data) {
    nv.addGraph(function() {
        chart = nv.models.lineChart()
                .useInteractiveGuideline(true)
                .showYAxis(true)
                .showXAxis(true);
        chart.xAxis
            .axisLabel("Time")
            .tickValues([0,1,2,3,4,5,6,7,8,9]);
        chart.yAxis
            .axisLabel("Distance")
            .axisLabelDistance(40);
        d3.select(id)
            .datum(data)
            .call(chart);
        nv.utils.windowResize(function() { 
            chart.update();
            //chart.height(window.innerHeight);
        });
        return chart;
    });
};

function getChampData(value) {
    console.log(value);
    var data = [], i;
    for (i = 0; i < 10; i++) {
        data.push({x:i, y:i});
    }
    // document.write(data);
    return [{values: data, key: "linegraph"}];
}