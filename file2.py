#sample cicd with ansible
node{
stage("gitclone"){
    git credentialsId: 'git-cred', url: 'https://github.com/njingu90/myapp-ansible.git'
}
stage("deploy-dev"){
    ansiblePlaybook credentialsId: 'digitalocean-1', disableHostKeyChecking: true, installation: 'ansible2', inventory: 'dev.inv', playbook: 'apache.yml'
}
stage("manaul-approval"){
    timeout(time:8, unit:'MINUTES'){
   input message: 'please verify and approve to deploy'
}}
stage("deploy-prod"){
   ansiblePlaybook credentialsId: 'digitalocean-1', disableHostKeyChecking: true, installation: 'ansible2', inventory: 'prod.inv', playbook: 'apache.yml'
}
}
