FROM openjdk:8-jdk

ADD app.jar /java/app.jar
ADD kdx.pem /java/kdx.pem

CMD ["java", "-Duser.timezone=Asia/Seoul", "-jar", "/java/app.jar"]
