# Tarefa Socket

Pequena aplicação para a tarefa de sockets da disciplina de Redes, que consiste de um Echo Server e o Cliente para o mesmo.

## Feito por: 
>[Caio Souza de Oliveira](https://github.com/caiosdeo)

## Echo Server

### Execução

Caso queira especificar o _host_ e a porta para executar seu _Echo Server_, poderá executar da seguinte forma:
```sh
python echo_server.py <host> <port>
```

Caso prefira usar localmente poderá executar com a opção local, utilizando _host_ e _port_ predefinidos:
```sh
python echo_server.py local
```

### Comandos
O Servidor é capaz de compreender dois comandos:

- echo <parametros>
- quit

#### Echo

O comando _echo_ possui um parametro no qual você poderá passar sua mensagem.
A mensagem chega no servidor e o mesmo retorna para o cliente imprimindo ela.

#### Quit

O comando _quit_ não possui parametros e ele encerra a conexão com o cliente.

## Echo Client

### Execução

A execução do cliente é semelhante ao servidor. Caso queira especificar o _host_ e a porta a qual desejar conectar, poderá executar da seguinte forma:
```sh
python echo_client.py <host> <port>
```
Caso prefira usar localmente poderá executar com a opção local, utilizando _host_ e _port_ predefinidos:
```sh
python echo_client.py local
```