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
        $('<div class="col-md-12">').append(
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
                                $('<option value="OVERALL">').html('Overall'),
                                $('<option value="BRONZE">').html('Bronze'),
                                $('<option value="SILVER">').html('Silver'),
                                $('<option value="GOLD">').html('Gold'),
                                $('<option value="PLATINUM">').html('Platinum'),
                                $('<option value="DIAMOND">').html('Diamond'),
                                $('<option value="MASTER">').html('Master'),
                                $('<option value="CHALLENGER">').html('Challenger')
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
                            $('<button class="btn btn-success" onclick="drawGraphs(' + count + ');">').html('Generate data')
                        )
                    ),
                    $('<div class="row">').append(
                        $('<div class="col-md-3">').append(
                            $('<div id="winRatio0' + count + '" style="height:200px;border-style:solid;border-width:5px;">').append(
                                ('<svg></svg>')
                            )
                        ),
                        $('<div class="col-md-3">').append(
                            $('<div id="popularity0' + count + '" style="height:200px;border-style:solid;border-width:5px;">').append(
                                ('<svg></svg>')
                            )
                        ),
                        $('<div class="col-md-3">').append(
                            $('<div id="winRatio1' + count + '" style="height:200px;border-style:solid;border-width:5px;">').append(
                                ('<svg></svg>')
                            )
                        ),
                        $('<div class="col-md-3">').append(
                            $('<div id="popularity1' + count + '" style="height:200px;border-style:solid;border-width:5px;">').append(
                                ('<svg></svg>')
                            )
                        )
                    ),
                    $('<div class="row">').append(
                        $('<div class="col-md-3">').append(
                            $('<div id="dmg0' + count + '" style="height:200px;border-style:solid;border-width:5px;">').append(
                                ('<svg></svg>')
                            )
                        ),
                        $('<div class="col-md-3">').append(
                            $('<div id="kda0' + count + '" style="height:200px;border-style:solid;border-width:5px;">').append(
                                ('<svg></svg>')
                            )
                        ),
                        $('<div class="col-md-3">').append(
                            $('<div id="dmg1' + count + '" style="height:200px;border-style:solid;border-width:5px;">').append(
                                ('<svg></svg>')
                            )
                        ),
                        $('<div class="col-md-3">').append(
                            $('<div id="kda1' + count + '" style="height:200px;border-style:solid;border-width:5px;">').append(
                                ('<svg></svg>')
                            )
                        )
                    )
                ),
                $('<div class="panel-footer">').append(
                    $('<div class="container">').append(
                        $('<div class="col-md-6" id="champList' + count + '">').append(

                        ),
                        $('<div class="col-md-3">').append(
                            $('<input class="inputarea" id="inputarea' + count + '" type="text" size="70" style="color:#000000;" onkeyup="showResult(this.value, ' + count + ')">'),
                            $('<div id="livesearch' + count + '">')
                        ),
                        $('<div class="col-md-3">').append(
                            $('<button class="btn btn-default" onclick="addChampion(' + count + ')">').html("Add Champ")
                        )
                    )
                )
            )
        )
    );
    count += 1;
}

function addChampion(id) {
    if ($('#champList' + id).children().length > 4) {
        alert("too many champs!");
        return null;
    }
    var name = document.getElementById('inputarea' + id).value;
    var champs = [];
    if (name == "") {
        return null;
    }
    $('#champList' + id).children().each(function() {
        champs.push(this.innerHTML);
    });
    if ($.inArray(name, champs) > -1) {
        alert("Champion already exists.");
        return null;
    }
    $('#champList' + id).append(
        $('<button class="btn btn-danger btn-lg" onclick="$(this).remove()">').html(name)
    );
    document.getElementById('inputarea' + id).value = "";
}

function selectRecommendation(html, id) {
    var search = "livesearch" + id;
    document.getElementById('inputarea' + id).value = html.innerHTML;
    addChampion(id);
    $('#' + search).empty();
}

function drawGraphs(id) {
    var champs = [];
    // var patch = document.getElementById("patch" + id).value;
    var region = document.getElementById("region" + id).value;
    var tier = document.getElementById("tier" + id).value;
    $('#champList' + id).children().each(function() {
        champs.push(this.innerHTML);
    });
    if (champs.length == 0) {
        alert("No champions selected!");
        return null;
    }
    var data0 = [];
    var data1 = [];
    for (var i=0; i < champs.length; i++) {
        var url = "../data/5.11/" + region + "/5.11-" + region + "-" + champs[i] + "-" + tier + ".json";
        $.get( url, function(champInfo) {
            data0.push(champInfo);
        });
        var url = "../data/5.14/" + region + "/5.14-" + region + "-" + champs[i] + "-" + tier + ".json";
        $.get( url, function(champInfo) {
            data1.push(champInfo);
        });
    }
    var data = [data0, data1];
    $(document).ajaxStop(function () {
        console.log(data);
        var kda11 = [];
        var dmg11 = [];
        var popularity11 = [];
        var winRatio11 = [];
        var patches = ["5.11", "5.14"];
        for (var j=0;j<patches.length;j++) {
            var allkda = [];
            var alldmg = [];
            var allpopularity = [];
            var allWinRatio = [];
            for(i=0;i<data[j].length;i++) {
                var picked = data[j][i]["pick"];
                var kills = data[j][i]["kills"];
                var deaths = data[j][i]["deaths"];
                var assists = data[j][i]["assists"];
                var totalDamage = data[j][i]["totalDamageDealtToChampions"];
                var magicDamage = data[j][i]["magicDamageDealtToChampions"];
                var goldEarned = data[j][i]["goldEarned"];
                var bans = data[j][i]["bans"];
                var wins = data[j][i]["wins"];
                var duration = data[j][i]["duration"];
                var dmg = 
                {"key":data[j][i]["name"] + patches[j], "values":[
                    {"x":"TotalDmg", "y":totalDamage/picked}, 
                    {"x":"MagicDmg", "y":magicDamage/picked}
                    ]
                };
                var kda = 
                {"key":data[j][i]["name"] + patches[j], "values":[
                    {"x":"Kills", "y":kills/picked}, 
                    {"x":"Deaths", "y":deaths/picked}, 
                    {"x":"Assists", "y":assists/picked},
                    {"x":"Overall", "y":(kills+assists)/picked}
                    ]
                };
                var popularity = 
                {"key":data[j][i]["name"] + patches[j], "values":[
                    {"x":"Picked", "y":picked}, 
                    {"x":"Banned", "y":bans},
                    {"x":"Duration", "y":duration/picked}
                    ]
                };
                var winRatio = 
                {"key":data[j][i]["name"] + patches[j], "values":[
                    {"x":"WinRate", "y":wins/picked * 100},
                    {"x":"PickRate", "y":picked/10000 * 100},
                    {"x":"BanRate", "y":bans/picked * 100}
                    ]
                };
                allkda.push(kda);
                alldmg.push(dmg);
                allpopularity.push(popularity);
                allWinRatio.push(winRatio);
            }
            kda11.push(allkda);
            dmg11.push(alldmg);
            popularity11.push(allpopularity);
            winRatio11.push(allWinRatio);
        }
        barGraph("#kda0" + id + " svg", kda11[0]);
        barGraph("#dmg0" + id + " svg", dmg11[0]);
        barGraph("#kda1" + id + " svg", kda11[1]);
        barGraph("#dmg1" + id + " svg", dmg11[1]);
        barGraph("#popularity0" + id + " svg", popularity11[0]);
        barGraph("#popularity1" + id + " svg", popularity11[1]);
        barGraph("#winRatio0" + id + " svg", winRatio11[0]);
        barGraph("#winRatio1" + id + " svg", winRatio11[1]);
    });
}

function circleGraph(id, data) {
    nv.addGraph(function() {
    var chart = nv.models.pieChart()
    .x(function(d) { return d.label })
    .y(function(d) { return d.value })
    .showLabels(true)     //Display pie labels
    .labelThreshold(.05)  //Configure the minimum slice size for labels to show up
    .labelType("percent") //Configure what type of data to show in the label. Can be "key", "value" or "percent"
    .donut(true)          //Turn on Donut mode. Makes pie chart look tasty!
    .donutRatio(0.35)     //Configure how big you want the donut hole size to be.
    ;

    d3.select(id)
    .datum(data)
    .transition().duration(350)
    .call(chart);

    return chart;
    });
}


function barGraph(id, data) {
    nv.addGraph(function() {
        var chart = nv.models.multiBarChart()
          .reduceXTicks(false)   //If 'false', every single x-axis tick label will be rendered.
          .rotateLabels(0)      //Angle to rotate x-axis labels.
          .groupSpacing(0.1)    //Distance between each group of bars.
          .showControls(false)
        ;

        d3.select(id)
            .datum(data)
            .call(chart);

        nv.utils.windowResize(chart.update);

        return chart;
    });

}