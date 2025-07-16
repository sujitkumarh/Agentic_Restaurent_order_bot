async function fetchMenu() {
    const res = await fetch('http://localhost:8080/menu');
    const data = await res.json();
    const menuList = document.getElementById('menu-list');
    menuList.innerHTML = '';
    data.menu.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.name} - $${item.price}`;
        menuList.appendChild(li);
    });
}

document.getElementById('voice-btn').onclick = async function() {
    const language = document.getElementById('language-select').value;
    // Simulate voice order (replace with real voice/NLU integration)
    const order = {
        items: [{menu_id: 1, modifiers: []}],
        dietary: [],
        language: language
    };
    const res = await fetch('http://localhost:8080/order', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(order)
    });
    const result = await res.json();
    document.getElementById('order-status').textContent = result.status === 'success' ? 'Order placed!' : result.message;
};

window.onload = fetchMenu;
