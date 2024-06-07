node (){
    stage("checkout"){
        git branch: 'main', url: 'https://github.com/shanimarco/WorldOfGames.git'
    }
    stage('Build image') {
          app = docker.build("WorldOfGames/main")
       }
}