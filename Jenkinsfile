pipeline {
    // 1. На чем запускать? (any - на любом свободном сервере/агенте)
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Скачиваем код из вашего GitHub
                git branch: 'develop2', url: 'https://github.com/VAMolodov/Diplom_2.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Создаем виртуальное окружение и ставим библиотеки
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Запускаем тесты. Не забудьте про --headless в коде фикстуры!
                sh '''
                    source venv/bin/activate
                    pytest --alluredir=allure-results
                '''
            }
        }
    }

    // 3. Что сделать после тестов?
    post {
        always {
            // Генерируем Allure отчет
            allure includeProperties: false, jdk: '', results: [[path: 'target/allure-results']]
        }
    }
}
