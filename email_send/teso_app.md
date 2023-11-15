"""

# Feature Logic

there will be a CSV file where all the current status of the clients will be stored.
Every month the program will:
- Read treasury CSV file and notifies users of their current status.
- Send a reminder to the clients with pending fees.
- Send a report to the treasurer with the current status of the club.
- Send a report to the president with the current status of the club.
Once the email is sent, the program will update the CSV file with the current date.

To check if the program is working, a test will assert that the CSV file has been updated with the current date.

Note: there are special cases where the client has paid in advance, or has paid more than the current fee. In those cases, the program will notify the client of the current status of their account.

--------------------------------------------------
The format of the message sent will change according to the status of the client: with debt, in favor, or at day.

STATUS 1: Debt. Client has pending shares to pay.
---
💰 MENSAJE DE TESORERÍA:

👋🏼 Buenas {name},
🌼 ¡LLEGÓ {month} y el valor de la cuota es {month_fee}!.

Tu saldo a pagar finalmente es de {client_debt} y corresponde a meses: {debt_month_list}. 

🤑 Podés transferir al siguiente alias RTC.CANIADA. Porfa no te olvides de completar el form con el comprobante una vez hecho el abono. A continuación el link: {link_form}

Gracias, tu teso prefe 🙆🏽‍♀️.

---
---

STATUS 2 in favor: client has shares to receive.
---
💰 MENSAJE DE TESORERÍA:

👋🏼 Buenas {name},
🌼 LLEGÓ {month} y el valor de la cuota es de {month_fee}.

Teniendo en cuenta que pagaste las cuotas de {month_list} de {year}, contás con $500 pesos a favor. Los mismos pueden ser devueltos o quedarte a favor para la cuota de Diciembre. Porfis avisame que preferís hacer.

Gracias, tu teso prefe 🙆🏽‍♀️.

---
---
STATUS 3: at day: client has no pending shares.
---
💰 MENSAJE DE TESORERÍA:

👋🏼 Buenas {name},
🌼 LLEGÓ {month} y el valor de la cuota es de {month_fee}.

Tu saldo a pagar es de $1.050 correspondiente a este mes, {month}. 

🤑 Podés transferir al siguiente alias RTC.CANIADA. Porfa no te olvides de completar el form con el comprobante una vez hecho el abono. A continuación el link: {link_form}

Gracias, tu teso prefe 🙆🏽‍♀️.

---
---

Other features pending:
---
- Checking club's balance
- Checking member's balance
- Updating values

"""