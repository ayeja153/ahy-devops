pipeline {
   agent any
   
   parameters{
    string(name:'image_name',defaultValue:'ayeja153/flask-app:v1', description:'Image name')
    string(name:'container_name',defaultValue:'flask-app', description:'Container name')
    string(name:'tag_name',defaultValue:'1', description:'Tag name')
    string(name:'port',defaultValue:'9000', description:'Port')
   }    
    stages {
        
    stage('Prepare') {
      steps {
         sh 'docker pull ${image_name}:${tag_name} && docker stop ${container_name} 2>/dev/null || true && docker rm -f ${container_name} 2>/dev/null || true'
      }
    }
    
    stage('Deploy') {
      steps {
        // Deploy the Docker container to a server
         sh 'docker run -d --name ${container_name} -p ${port}:8080 ${image_name}:${tag_name}'
       }
    }
  }
}
