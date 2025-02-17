// This is your test secret API key.
const stripe = Stripe("pk_test_51QsjeH02ahKmoBWWiupTVTSOypH3073b25gWzF4vB0vk9SIvAWpCFPVkE5Dp5P2R6eNmvBRevBxR07Xzyv1QHV6s00IWGTX1Cx");

initialize();

document.write("Hello, World! checkout static");
console.log("Sanity check! checkout folder");

// Create a Checkout Session
async function initialize() {
    const fetchClientSecret = async () => {
        const response = await fetch("/checkout/create-checkout-session/", {
            method: "POST",
        });
        const { clientSecret } = await response.json();
        return clientSecret;
    };

    const checkout = await stripe.initEmbeddedCheckout({
        fetchClientSecret,
    });

    // Mount Checkout
    checkout.mount('#checkout');
}