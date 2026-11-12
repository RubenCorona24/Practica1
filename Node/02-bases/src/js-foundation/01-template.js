
//creamos un email template
const emailTemplate = `
<div>
    <h1>Hi, {{name}}</h1>
    <p>Than you for your order.</p>
    <p>Order ID: {{orderId}}.</p>
</div>
`
//exportamos nuestro email template
module.exports = {
    emailTemplate
}