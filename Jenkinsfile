pipeline
{
    agent
    {
        label 'retail'
    }
   //agent any
    stages
    {
//          stage('Clone repository')
//              {
//                 steps
//                 {
//                    script
//                    {
//                       withCredentials([file(credentialsId: 'search-console-env', variable: 'vars_data')])
//                     {
//                         sh "cp $vars_data .env"
//                         checkout scm
//                     }
//                    }
//                 }
//             }
//         stage('Build')
//         {
//             steps
//             {
//                 script
//                 {
//                     sh "docker-compose down"
//                     sh "docker-compose build"
//                     // app = docker.image("dashboard-mf-ui:latest")
//                 }
//             }
//         }
        stage('Deploy Dev')
        {
            steps
            {
                script
                {
                    sh "echo hello"
                }
            }
        }
    }
}
