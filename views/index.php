<?php?>

<!DOCTYPE html>
<html>
    <head>
        <title>API-tems</title>
        <meta charset="utf-8">
        <script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
        <link rel="shortcut icon" href="http://ddragon.leagueoflegends.com/cdn/5.2.1/img/item/3089.png">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
        <script src="js/app.js"></script>
        <link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Open+Sans:300,400,600">
        <link rel="stylesheet" href="css/styles.css">
        <link rel="stylesheet" href="js/nvd3/nv.d3.css">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.2/d3.min.js" charset="utf-8"> </script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.0/js/materialize.min.js"> </script>
        <script src="js/nvd3/nv.d3.min.js"></script>
    </head>

    <body>
        <div class="background">
            <div class="hero">
                <div class="container">
                    <nav class="row">
                        <div class="col-md-12">
                            <a href="#" class="link">Home</a>
                            <a href="#" class="link" id="about">About</a>
                        </div>
                    </nav>
                    <div class="row">
                        <div class="col-md-10"> 
                            <h1>API-tems</h1>
                            <h2>Pre and Post AP Item Change Statistics</h2>
                        </div>
                        <button onclick="createPanel()">Create Panel!</button>
                        <button class="btn btn-success" onclick="createPanel()">Create Panel!</button>
                        <script>createPanel()</script>
                    </div>
                </div>
            </div>
        </div>


        <div class="container">
            <div class="col-md-3">
            </div>
        </div>
        <div class="footer">
            <div class="container">
                <div class="row">
                    <div class="col-md-12">
                        <h3> Created by <a id="bryan"> Bryan Yan </a> and <a id="warren"> Warren Tian </a> </h3>
                    </div>
                    <div class="col-md-12">
                        <h4>API-tems isn’t endorsed by Riot Games and doesn’t reflect the views or opinions of Riot Games or anyone officially involved in producing or managing League of Legends. League of Legends and Riot Games are trademarks or registered trademarks of Riot Games, Inc. League of Legends © Riot Games, Inc. </h4>
                    </div>
                </div>
            </div>
        </div>
    </body>
</html>
