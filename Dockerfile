FROM ubuntu:20.04

#==============
# Update package manager
#==============
RUN apt-get update \
 && apt-get install -y python3-pip



#=================
# Display python and pip
#=================
RUN python3 --version \
 && pip3 --version

#=================
# Enable port 9099
#=================
EXPOSE 9099

WORKDIR /restful-booker-collector
#=================
# Install requirements
#=================
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
#=================
# Add run.sh to the image and change
#=================
#ADD run.sh run.sh
#RUN sed -i 's/\r$//' run.sh
#RUN chmod +x run.sh
#COPY custom_collector_package /custom_collector_package
COPY . /restful-booker-package
#CMD "./run.sh"
CMD python3 restful_booker_collector.py