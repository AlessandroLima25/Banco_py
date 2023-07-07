# Banco New

🏦🌟

This is a simple program that simulates a banking system. It allows users to perform operations such as withdrawal, deposit, and view the account statement.

## How to Use

🔧📋

1. Run the code in a Python environment.
2. Follow the instructions displayed in the menu to select the desired operation.
3. Enter the requested information, such as the deposit amount or withdrawal quantity.
4. The program will process the operation and display informative messages about the result.
5. After completing each operation, you will be redirected back to the menu to select a new option.
6. To exit the program, select the "q" option in the menu.

## Features

⚙️📄

The program offers the following features:

- **Withdraw (s)**: Allows you to withdraw a specific amount of money from the account. It checks for sufficient balance, available limit, and exceeded withdrawal limit before completing the operation.
- **Deposit (d)**: Allows you to make a deposit into the account. It checks if the deposit amount is positive before completing the operation.
- **Statement (e)**: Displays the account statement, showing all the operations performed and the current balance.
- **Quit (q)**: Exits the program.

## Variables

🔢📊

The program uses the following variables:

- `saldo` (balance): Stores the current account balance.
- `limite` (limit): Stores the available withdrawal limit.
- `extrato` (statement): Stores the history of operations performed.
- `numero_saques` (num_withdrawals): Stores the number of withdrawals made.
- `LIMITE_SAQUES` (WITHDRAWAL_LIMIT): Stores the maximum number of withdrawals allowed.

## Example

🔍📝

Here's an example of using the program:

```
*******************Banco New*******************
Welcome to our banking system!
Please enter the initials below to perform operations!

[s] Sacar (Withdraw)
[d] Depositar (Deposit)
[e] Extrato (Statement)
[q] Sair (Quit)

***********************************************
=>s
*******************Banco New*******************
Opção de saque selecionada! (Withdraw option selected!)
Digite a quantidade para sacar: 50 (Enter the amount to withdraw: 50)

Aguarde enquanto processamos seu pedido... (Please wait while we process your request...)
Saque realizado com sucesso! (Withdrawal successful!)

A sua conta agora possui um novo saldo de R$450.00 (Your account now has a new balance of $450.00)
Confira o Extrato para mais detalhes! (Check the Statement for more details!)
Retornando para a tela inicial... Aguarde... (Returning to the main screen... Please wait...)
```

## Notes

⚠️📝

- Make sure to enter valid values when making deposits or withdrawals.

🌟🏦🌟

