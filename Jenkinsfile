node (){
    stage("checkout"){
        git branch: 'main', url: 'https://github.com/shanimarco/WorldOfGames.git'
    }
    stage('Build image') {
          sh 'docker build -t world_of_games_image .'
       }
}