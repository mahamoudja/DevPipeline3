pipeline{
    agent any
    
    stages {
        stage('Find and kill process') {
            steps {
            sh '''  var=$(pgrep -f hello)
                    kill -9 $var
                    '''
            }
        
        }
        
       stage('Pull code') {
            steps {
            sh 'git pull git@github.com:FDevBaig/DevPipeline3.git'
            }
        
        }
      
      
       stage('Build and run') {
            steps {
            sh '''  JENKINS_NODE_COOKIE=dontKillMe
                    nohup python3 hello_world.py &
                    '''
            }
        
        }
    
    }

}
