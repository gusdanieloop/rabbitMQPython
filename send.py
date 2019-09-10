#!/usr/bin/env python3
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))

#connection = pika.BlockingConnection(pika.ConnectionParameters(
#        host='localhost',
#        credentials=pika.PlainCredentials(username="sdi", password="sdi")))
channel = connection.channel()


channel.queue_declare(queue='maphello')

while(True):
        print('Digite uma mensagem!');
        mensagem = input()
        channel.basic_publish(exchange='',
                      routing_key='maphello',
                      body=mensagem)
        print(" [x] Sent " + mensagem)
        print("Deseja enviar mais uma mensagem? Sim - 1 Nao - 0")
        continuar = int(input())
        if(continuar == 0):
                break
connection.close()
