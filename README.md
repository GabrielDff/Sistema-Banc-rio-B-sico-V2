# Sistema Bancário Básico V2

### Este projeto consiste na implementação em **Python** de 5 funcionalidades (depósito, saque, visualização de extrato, cadastro de usuário e criação de conta) básicas de um sistema bancário, por meio de funções.

Vale ressaltar que, por se tratar de um sistema bem básico, não é solicitado nenhum tipo de credencial para acesso, além de que as operações de depósito não solicitam informações sobre a conta de destino. Ao iniciar, o usuário imediatamente recebe uma mensagem de boas vindas seguida de uma solicitação para escolha de uma das opções, sendo elas:

- **[D] Depósito:** o usuário deve indicar o valor para depósito.
- **[S] Saque:** o usuário deve indicar o valor a ser sacado, devendo ser observadas as restrições para realização de um saque.
- **[E] Extrato:** o usuário recebe na tela o extrato completo com todas os depósitos e saques realizados. Caso não tenha sido realizada nenhuma operação ainda, o usuário recebe uma mensagem informando isso.
- **[C] Cadastrar usuário:** o usuário deve fornecer o CPF para cadastro. Após a verificação se o CPF está disponível, o programa solicita o nome, data de nascimento e endereço do usuário (ou acusa que o CPF não está disponível). É exibida uma mensagem indicando se o cadastro foi realizado ou não.
- **[A] Criar conta:** o usuário deve fornecer o CPF para a criação de conta. Após a verificação se o CPF consta no cadastro de clientes, o programa atribui à conta o número de agência 0001 e um número de conta conforme a disponibilidade (ou acusa que o CPF não consta no cadastro de clientes). É exibida uma mensagem indicando se a conta foi criado ou não.
- **[0] Sair:** o usuário encerra a execução do programa, o que acarreta o fim de todas as informações sobre saldo, depósito e saque.

Ao informar valores pelo teclado, o usuário deve utilizar "." para separar a parte inteira das casas decimais.
