node (){
    stage("checkout"){
        git branch: 'main', url: 'https://github.com/shanimarco/WorldOfGames.git'
    }
    stage('Build image') {
          bat 'docker build -t world_of_games_image .'
       }
    stage('run image') {
          bat 'docker run -p 8777:5001 world_of_games_image'
       }
}