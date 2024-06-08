node (){
    stage('Checkout') {
            git branch: 'main' ,url: 'https://github.com/shanimarco/WorldOfGames.git'
        }
    stage('Build') {
        bat 'docker build -t world_of_games_image .'
    }
    stage('Test') {
        parallel(
            run: {
                bat 'docker run -p 8777:5001 world_of_games_image'
            },
            test: {
                bat 'python tests/e2e.py'
                bat 'curl localhost:8777/stopServer'
            }
        )
    }
}