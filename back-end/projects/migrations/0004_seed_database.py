from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0003_alter_certificate_certifying_institution"),
    ]

    operations = [
        migrations.RunSQL(
            sql=[
                (
                    '''INSERT INTO `projects_profile` VALUES (1,'Fernando Barreto Costa','https://github.com/fernando-costa','https://www.linkedin.com/in/fernando-barreto-costa/','Web developer with a multifaceted background, blending expertise in law, management, and software engineering to deliver unique and comprehensive solutions. Trained in an intensive web development program at Trybe, encompassing over 1,500 hours of learning and 30 hands-on, problem-based projects. Based in Salvador, Bahia, Brazil, I am excited to explore new opportunities and collaborations to achieve impactful results.');'''
                )
            ],
            reverse_sql=[
                (
                    "DELETE FROM `projects_profile` WHERE id=%s;",
                    [1]
                )
            ]
        ),
        migrations.RunSQL(
            sql=[
                (
                    '''INSERT INTO `projects_project` VALUES (1,'Django Portfolio','Full Stack project developed as a challenge for the Elective Python module at Trybe Web Development course. A dockerized application that uses Django Templates to render, in plain HTML and CSS, a Portfolio web site with data sourced from a MySQL database by its REST Framework API through HTTP requests.','https://github.com/fernando-costa/django-portfolio/','Django, DRF, JWT, MySQL','Full Stack, Python, Docker',1),(2,'Football Manager','Full Stack project developed as a challenge for completing the Back-End module at Trybe s Web Development course. It aims to integrate an HTTP server - application programming interface (API) implementing a RESTful pattern as a Back-End, developed using Typescript with Express, MySQL and Sequelize - to an user interface service - website Front-End, developed in React - using Docker to containerize and orchestrate the solution: a football tournment management app','https://github.com/fernando-costa/football-manager','Typescript, REST, API, Sequelize, Docker','Full Stack, Compose, React',1);'''
                )
            ],
            reverse_sql=[
                (
                    "DELETE FROM `projects_project` WHERE profile_id=%s;",
                    [1]
                )
            ]
        ),
        migrations.RunSQL(
            sql=[
                (
                    '''INSERT INTO `projects_certifyinginstitution` VALUES (1,'Trybe','https://www.credential.net/profile/fernandobarretocosta586463/wallet');'''
                )
            ],
            reverse_sql=[
                (
                    "DELETE FROM `projects_certifyinginstitution` WHERE id=%s;",
                    [1]
                )
            ]
        ),
        migrations.RunSQL(
            sql=[
                (
                    '''INSERT INTO `projects_certificate` VALUES (1,'Web Development Fundamentals','2024-07-30 17:27:32.899115',1),(2,'Front-End Development','2024-07-30 17:27:32.909231',1),(3,'Back-End Development','2024-07-30 17:27:32.915381',1),(4,'Computer Science Fundamentals','2024-07-30 17:27:32.922289',1),(5,'Python for Web Development','2024-07-30 17:27:32.928045',1),(6,'Full-Stack Web Development','2024-07-30 17:27:32.934134',1);'''
                )
            ],
            reverse_sql=[
                (
                    "DELETE FROM `projects_certificate` WHERE certifying_institution_id=%s;",
                    [1]
                )
            ]
        ),
        migrations.RunSQL(
            sql=[
                (
                    "INSERT INTO `projects_certificate_profiles` VALUES (1,1,1),(2,2,1),(3,3,1),(4,4,1),(5,5,1),(6,6,1);"
                )
            ],
            reverse_sql=[
                (
                    "DELETE FROM `projects_certificate_profiles` WHERE profile_id=%s;",
                    [1]
                )
            ]
        ),
    ]
