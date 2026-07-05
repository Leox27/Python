import os
import uuid
from datetime import datetime
import google.generativeai as genai
from flask import Flask, request, jsonify, session
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

import google.generativeai as genai

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)
# Secret key is required for Flask sessions (shopping cart) to work securely
app.secret_key = "premium_mart_ultra_secure_key"

# 20 Premium Luxury Demo Products
PRODUCTS = [
    {"id": 1, "name": "Premium Chronograph", "category": "Watches", "price": 4500, "discount": 10, "rating": 4.9, "stock": "In Stock", "desc": "Swiss automatic movement, sapphire crystal.", "img": "https://images.unsplash.com/photo-1523170335258-f5ed11844a49?auto=format&fit=crop&w=400&q=80"},
    {"id": 2, "name": "Midnight Leather Tote", "category": "Bags", "price": 1200, "discount": 0, "rating": 4.8, "stock": "Low Stock", "desc": "Handcrafted full-grain Italian leather.", "img": "https://images.unsplash.com/photo-1584916201218-f4242ceb4809?auto=format&fit=crop&w=400&q=80"},
    {"id": 3, "name": "Oud Wood Extrait", "category": "Perfumes", "price": 350, "discount": 5, "rating": 5.0, "stock": "In Stock", "desc": "Rare agarwood, cardamom, and sensual rosewood.", "img": "https://images.unsplash.com/photo-1594035910387-fea47794261f?auto=format&fit=crop&w=400&q=80"},
    {"id": 4, "name": "Diamond Solitaire", "category": "Jewelry", "price": 2800, "discount": 15, "rating": 4.9, "stock": "In Stock", "desc": "1 Carat flawless diamond set in platinum.", "img": "https://images.unsplash.com/photo-1599643478524-fb66f4534731?auto=format&fit=crop&w=400&q=80"},
    {"id": 5, "name": "Gold Silk Scarf", "category": "Accessories", "price": 250, "discount": 0, "rating": 4.7, "stock": "In Stock", "desc": "100% pure mulberry silk, artisan pattern.", "img": "https://images.unsplash.com/photo-1606760227091-3dd870d97f1d?auto=format&fit=crop&w=400&q=80"},
    {"id": 6, "name": "Celestial Tourbillon", "category": "Watches", "price": 12500, "discount": 0, "rating": 5.0, "stock": "Out of Stock", "desc": "Exquisite tourbillon with a meteorite dial.", "img": "https://images.unsplash.com/photo-1614164185128-e4ec99c436d7?auto=format&fit=crop&w=400&q=80"},
    {"id": 7, "name": "Velvet Evening Clutch", "category": "Bags", "price": 850, "discount": 10, "rating": 4.6, "stock": "In Stock", "desc": "Rich dark brown velvet with soft gold clasp.", "img": "https://images.unsplash.com/photo-1566150905458-1bf1fc113f0d?auto=format&fit=crop&w=400&q=80"},
    {"id": 8, "name": "Jasmine Bloom EDP", "category": "Perfumes", "price": 290, "discount": 0, "rating": 4.8, "stock": "In Stock", "desc": "Fresh night-blooming jasmine and vanilla.", "img": "https://images.unsplash.com/photo-1588405748880-12d1d2a59f75?auto=format&fit=crop&w=400&q=80"},
    {"id": 9, "name": "Platinum Bracelet", "category": "Jewelry", "price": 5400, "discount": 5, "rating": 4.9, "stock": "Low Stock", "desc": "Radiant cut diamonds enveloping your wrist.", "img": "https://images.unsplash.com/photo-1611591437281-460bfbe1220a?auto=format&fit=crop&w=400&q=80"},
    {"id": 10, "name": "Cashmere Wrap", "category": "Accessories", "price": 420, "discount": 0, "rating": 4.9, "stock": "In Stock", "desc": "Ethically sourced Mongolian cashmere.", "img": "https://images.unsplash.com/photo-1618354691422-b2ce13d78c3b?auto=format&fit=crop&w=400&q=80"},
    {"id": 11, "name": "Obsidian Diver", "category": "Watches", "price": 3200, "discount": 20, "rating": 4.7, "stock": "In Stock", "desc": "Water resistant up to 500m, matte finish.", "img": "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?auto=format&fit=crop&w=400&q=80"},
    {"id": 12, "name": "Saffiano Briefcase", "category": "Bags", "price": 1400, "discount": 0, "rating": 4.8, "stock": "In Stock", "desc": "Professional luxury for the modern executive.", "img": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?auto=format&fit=crop&w=400&q=80"},
    {"id": 13, "name": "Amber Dusk Cologne", "category": "Perfumes", "price": 310, "discount": 10, "rating": 4.6, "stock": "In Stock", "desc": "Warm amber and spices for a majestic aura.", "img": "https://images.unsplash.com/photo-1594035910387-fea47794261f?auto=format&fit=crop&w=400&q=80"},
    {"id": 14, "name": "Emerald Cut Ring", "category": "Jewelry", "price": 4100, "discount": 0, "rating": 4.9, "stock": "Low Stock", "desc": "Stunning 2-carat emerald with pave diamonds.", "img": "https://images.unsplash.com/photo-1605100804763-247f67b2548e?auto=format&fit=crop&w=400&q=80"},
    {"id": 15, "name": "Driving Gloves", "category": "Accessories", "price": 180, "discount": 0, "rating": 4.5, "stock": "In Stock", "desc": "Supple nappa leather designed for comfort.", "img": "https://images.unsplash.com/photo-1510425463958-dcced28da480?auto=format&fit=crop&w=400&q=80"},
    {"id": 16, "name": "Rose Gold Minimalist", "category": "Watches", "price": 2100, "discount": 15, "rating": 4.7, "stock": "In Stock", "desc": "Ultra-thin profile with a rose gold mesh band.", "img": "https://images.unsplash.com/photo-1524805444758-089113d48a6d?auto=format&fit=crop&w=400&q=80"},
    {"id": 17, "name": "Canvas Weekender", "category": "Bags", "price": 950, "discount": 0, "rating": 4.8, "stock": "In Stock", "desc": "Perfect travel companion merging style and utility.", "img": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?auto=format&fit=crop&w=400&q=80"},
    {"id": 18, "name": "Vanilla Orchid Mist", "category": "Perfumes", "price": 260, "discount": 0, "rating": 4.5, "stock": "In Stock", "desc": "Sweet, subtle, and sophisticated all-day wear.", "img": "https://images.unsplash.com/photo-1588405748880-12d1d2a59f75?auto=format&fit=crop&w=400&q=80"},
    {"id": 19, "name": "Pearl Drop Earrings", "category": "Jewelry", "price": 1200, "discount": 10, "rating": 4.9, "stock": "Low Stock", "desc": "Authentic Tahitian pearls set in white gold.", "img": "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?auto=format&fit=crop&w=400&q=80"},
    {"id": 20, "name": "Polarized Aviators", "category": "Accessories", "price": 380, "discount": 0, "rating": 4.6, "stock": "In Stock", "desc": "Timeless silhouette with premium UV protection.", "img": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=400&q=80"}
]

HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Premium Mart | Pure Elegance</title>
    <style>
        :root {
            --bg-creamy: #FFF8F0;
            --coffee: #6F4E37;
            --dark-brown: #3D2B1F;
            --beige: #F5EBDD;
            --soft-gold: #C9A227;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }
        body { background: var(--bg-creamy); color: var(--dark-brown); scroll-behavior: smooth; overflow-x: hidden; }

        /* Glassmorphism */
        .glass {
            background: rgba(245, 235, 221, 0.7);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.4);
            box-shadow: 0 8px 32px 0 rgba(61, 43, 31, 0.1);
        }
        
        .btn { background: var(--coffee); color: white; padding: 10px 24px; border: none; border-radius: 8px; cursor: pointer; transition: all 0.3s; font-weight: bold; }
        .btn:hover { background: var(--dark-brown); transform: translateY(-2px); box-shadow: 0 4px 10px rgba(0,0,0,0.2); }
        .btn-gold { background: var(--soft-gold); }
        .btn-gold:hover { background: #b08d22; }

        /* Navigation */
        nav { position: sticky; top: 0; z-index: 1000; display: flex; justify-content: space-between; padding: 1.2rem 3rem; align-items: center; }
        .logo { font-size: 1.8rem; font-weight: 800; color: var(--coffee); letter-spacing: 1px; cursor: pointer; }
        .nav-links a { color: var(--dark-brown); text-decoration: none; font-weight: 600; margin-left: 2rem; transition: color 0.3s; padding-bottom: 5px; border-bottom: 2px solid transparent; }
        .nav-links a:hover, .nav-links a.active { color: var(--soft-gold); border-bottom: 2px solid var(--soft-gold); }
        .hamburger { display: none; font-size: 24px; cursor: pointer; background: none; border: none; }

        /* Hero */
        .hero { position: relative; min-height: 80vh; display: flex; align-items: center; padding: 4rem; overflow: hidden; background: linear-gradient(135deg, var(--bg-creamy), var(--beige)); border-radius: 30px; margin: 20px;}
        .hero-content { position: relative; z-index: 2; max-width: 600px; animation: slideUp 1s ease; }
        .hero h1 { font-size: 4rem; color: var(--coffee); margin-bottom: 1rem; line-height: 1.1; }
        .hero p { font-size: 1.2rem; margin-bottom: 2rem; opacity: 0.8; }
        .hero-banner { display: inline-block; background: var(--soft-gold); color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem; margin-bottom: 1rem; font-weight: bold; }
        
        .shape { position: absolute; border-radius: 50%; background: linear-gradient(135deg, var(--soft-gold), var(--beige)); opacity: 0.3; filter: blur(60px); z-index: 0; }
        .shape1 { width: 400px; height: 400px; top: -100px; right: -50px; animation: float 6s infinite alternate; }
        .shape2 { width: 300px; height: 300px; bottom: -50px; left: -50px; animation: float 8s infinite alternate-reverse; }
        
        /* Layout */
        .view-section { display: none; padding: 2rem; max-width: 1400px; margin: 0 auto; min-height: 80vh; }
        .view-section.active { display: block; animation: fadeIn 0.6s ease; }

        /* Product Cards */
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px; margin-top: 2rem; }
        .card { border-radius: 20px; overflow: hidden; transition: all 0.4s ease; position: relative; display: flex; flex-direction: column; background: white; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
        .card:hover { transform: translateY(-10px); box-shadow: 0 20px 40px rgba(61, 43, 31, 0.15); }
        .card-img { height: 280px; background-size: cover; background-position: center; position: relative; cursor: pointer; }
        .badge { position: absolute; top: 15px; left: 15px; background: #e74c3c; color: white; padding: 5px 10px; border-radius: 10px; font-weight: bold; font-size: 0.8rem; }
        .card-body { padding: 20px; display: flex; flex-direction: column; flex-grow: 1; }
        .category { font-size: 0.8rem; color: var(--soft-gold); text-transform: uppercase; font-weight: bold; margin-bottom: 5px; }
        .title { font-size: 1.2rem; font-weight: 700; margin-bottom: 10px; }
        .price-row { display: flex; justify-content: space-between; align-items: center; margin: 15px 0; }
        .price { font-size: 1.4rem; font-weight: bold; color: var(--coffee); }
        .original-price { text-decoration: line-through; color: #999; font-size: 0.9rem; margin-right: 10px; }
        .actions { display: flex; gap: 10px; margin-top: auto; }
        .actions button { flex: 1; }
        .actions .btn-icon { flex: 0 0 50px; background: var(--beige); color: var(--coffee); }

        /* Tables & Cart */
        .table-container { background: white; border-radius: 20px; padding: 2rem; overflow-x: auto; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
        table { width: 100%; border-collapse: collapse; min-width: 600px; }
        th, td { padding: 15px; text-align: left; border-bottom: 1px solid var(--beige); }
        .qty-controls { display: flex; align-items: center; gap: 10px; }
        .qty-btn { background: var(--beige); border: none; width: 30px; height: 30px; border-radius: 50%; cursor: pointer; font-weight: bold; }
        .cart-summary { margin-top: 2rem; text-align: right; background: white; padding: 2rem; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
        .order-card { padding: 2rem; border-radius: 20px; margin-bottom: 2rem; border-left: 5px solid var(--soft-gold); background: white;}
        
        /* Modals */
        .modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.5); backdrop-filter: blur(5px); z-index: 2000; display: none; align-items: center; justify-content: center; opacity: 0; transition: opacity 0.3s; }
        .modal-box { padding: 3rem; border-radius: 25px; width: 90%; max-width: 500px; position: relative; transform: scale(0.9); transition: transform 0.3s; background: white;}
        .modal-close { position: absolute; top: 15px; right: 20px; background: none; border: none; font-size: 1.5rem; cursor: pointer; color: var(--dark-brown); }
        .form-group { margin-bottom: 15px; }
        .form-group input { width: 100%; padding: 12px; border: 1px solid var(--beige); border-radius: 8px; outline: none; }

        /* Footer */
        footer { background: var(--dark-brown); color: var(--beige); padding: 4rem 2rem 2rem; text-align: center; }
        .footer-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 30px; text-align: left; max-width: 1200px; margin: 0 auto 3rem; }
        footer a { color: var(--beige); text-decoration: none; opacity: 0.8; display: block; margin-bottom: 10px; }
        footer a:hover { color: var(--soft-gold); opacity: 1; }

        /* Chatbot */
        #chat-widget { position: fixed; bottom: 30px; right: 30px; z-index: 1500; }
        #chat-btn { width: 65px; height: 65px; border-radius: 50%; background: var(--soft-gold); color: white; font-size: 28px; border: none; cursor: pointer; box-shadow: 0 10px 25px rgba(201, 162, 39, 0.4); animation: float 3s infinite alternate; display: flex; align-items: center; justify-content: center; }
        #chat-window { display: none; width: 380px; height: 600px; border-radius: 20px; flex-direction: column; overflow: hidden; box-shadow: 0 15px 40px rgba(0,0,0,0.2); transform-origin: bottom right; animation: scaleUp 0.3s ease; background: white;}
        #chat-header { background: var(--coffee); color: white; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; font-weight: bold; }
        #chat-messages { flex: 1; padding: 20px; overflow-y: auto; display: flex; flex-direction: column; gap: 15px; background: var(--bg-creamy); }
        .msg { padding: 12px 16px; border-radius: 15px; max-width: 85%; font-size: 0.95rem; line-height: 1.4; }
        .msg.user { background: var(--beige); align-self: flex-end; border-bottom-right-radius: 2px; }
        .msg.ai { background: var(--soft-gold); color: white; align-self: flex-start; border-bottom-left-radius: 2px; }
        #chat-input-area { display: flex; padding: 15px; background: white; border-top: 1px solid var(--beige); }
        #chat-input-area input { flex: 1; padding: 12px; border: 1px solid var(--beige); border-radius: 25px; outline: none; }
        #chat-input-area button { background: var(--coffee); color: white; border: none; width: 40px; height: 40px; border-radius: 50%; margin-left: 10px; cursor: pointer; }
        .typing { display: inline-block; animation: blink 1.4s infinite both; }

        /* Animations */
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
        @keyframes slideUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }
        @keyframes float { from { transform: translateY(0); } to { transform: translateY(-10px); } }
        @keyframes scaleUp { from { opacity: 0; transform: scale(0.8); } to { opacity: 1; transform: scale(1); } }
        @keyframes blink { 0% { opacity: .2; } 20% { opacity: 1; } 100% { opacity: .2; } }

        /* Toast */
        #toast { position: fixed; top: 20px; left: 50%; transform: translateX(-50%); background: var(--coffee); color: white; padding: 15px 30px; border-radius: 30px; font-weight: bold; z-index: 3000; display: none; box-shadow: 0 10px 20px rgba(0,0,0,0.2); }

        @media (max-width: 768px) {
            .nav-links { display: none; position: absolute; top: 100%; left: 0; right: 0; background: var(--bg-creamy); flex-direction: column; padding: 20px; text-align: center; }
            .nav-links.show { display: flex; box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
            .nav-links a { margin: 10px 0; }
            .hamburger { display: block; }
            .hero h1 { font-size: 2.5rem; }
            #chat-window { width: 90vw; height: 70vh; bottom: 90px; right: 5vw; }
        }
    </style>
</head>
<body>
    <div id="toast"></div>

    <nav class="glass">
        <div class="logo" onclick="navigate('home')">✨ Premium Mart</div>
        <button class="hamburger" onclick="document.querySelector('.nav-links').classList.toggle('show')">☰</button>
        <div class="nav-links">
            <a href="#" id="nav-home" onclick="navigate('home')">🏠 Home</a>
            <a href="#" id="nav-products" onclick="navigate('products')">🛍 Vault</a>
            <a href="#" id="nav-cart" onclick="navigate('cart')">🛒 Cart (<span id="cart-count">0</span>)</a>
            <a href="#" id="nav-orders" onclick="navigate('orders')">📦 Orders</a>
            <a href="#" onclick="showLogin()">👤 Login</a>
        </div>
    </nav>

    <div id="view-home" class="view-section active">
        <div class="hero glass">
            <div class="shape shape1"></div>
            <div class="shape shape2"></div>
            <div class="hero-content">
                <span class="hero-banner">Exclusive Autumn Release</span>
                <h1>Discover Pure Elegance</h1>
                <p>Elevate your lifestyle with our curated collection of luxury watches, designer bags, and exotic perfumes.</p>
                <button class="btn btn-gold" style="font-size: 1.1rem;" onclick="navigate('products')">Explore Collection</button>
            </div>
        </div>
        <h2 style="margin-top: 4rem; text-align: center;">Featured Selections</h2>
        <div class="grid" id="featured-grid"></div>
    </div>

    <div id="view-products" class="view-section">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem; flex-wrap: wrap; gap: 15px;">
            <h2>The Premium Mart Vault</h2>
            <input type="text" id="search-box" placeholder="Search premium item..." style="padding: 10px 20px; border-radius: 20px; border: 1px solid var(--beige); outline: none; width: 300px; max-width: 100%;" onkeyup="renderProducts(this.value)">
        </div>
        <div class="grid" id="products-grid"></div>
    </div>

    <div id="view-cart" class="view-section">
        <h2>Your Shopping Bag</h2>
        <div id="cart-container" style="margin-top: 2rem;"></div>
    </div>

    <div id="view-orders" class="view-section">
        <h2>Order History</h2>
        <div id="orders-container" style="margin-top: 2rem;"></div>
    </div>

    <div id="modal-overlay" class="modal-overlay" onclick="closeModal()">
        <div id="modal-content" class="modal-box glass" onclick="event.stopPropagation()">
            <button class="modal-close" onclick="closeModal()">×</button>
            <div id="modal-body"></div>
        </div>
    </div>

    <footer>
        <div class="footer-grid">
            <div>
                <h3 style="color: var(--soft-gold); margin-bottom: 1rem;">✨ Premium Mart</h3>
                <p>Curators of fine items and exquisite taste since 2026.</p>
            </div>
            <div>
                <h3 style="margin-bottom: 1rem;">Quick Links</h3>
                <a href="#" onclick="navigate('products')">Shop Collection</a>
                <a href="#">About Premium Mart</a>
            </div>
            <div>
                <h3 style="margin-bottom: 1rem;">Newsletter</h3>
                <div style="display: flex; gap: 10px;">
                    <input type="email" placeholder="Email Address" style="padding: 10px; border-radius: 5px; border:none; width: 100%; outline: none;">
                    <button class="btn btn-gold" onclick="showToast('Subscribed Successfully!')">Join</button>
                </div>
            </div>
        </div>
        <p style="opacity: 0.5;">© 2026 Premium Mart. All rights reserved.</p>
    </footer>

    <div id="chat-widget">
        <button id="chat-btn" onclick="toggleChat()">✨</button>
        <div id="chat-window">
            <div id="chat-header">
                Concierge AI
                <button onclick="toggleChat()" style="background:none;border:none;color:white;cursor:pointer;font-size:1.2rem;">—</button>
            </div>
            <div id="chat-messages">
                <div class="msg ai">Welcome to Premium Mart! I am your AI Concierge. How may I assist you today?</div>
            </div>
            <div id="chat-input-area">
                <input type="text" id="chat-input" placeholder="Ask anything..." onkeypress="if(event.key==='Enter') sendChat()">
                <button onclick="sendChat()">➤</button>
            </div>
        </div>
    </div>

    <script>
        // Central State
        let STATE = {
            products: [],
            cart: {},
            orders: []
        };

        // Application Bootstrapper
        window.onload = async () => {
            try {
                const response = await fetch('/api/init');
                const data = await response.json();
                STATE.products = data.products;
                STATE.cart = data.cart;
                STATE.orders = data.orders;
                
                updateCartCount();
                renderProducts();
                renderFeatured();
                navigate('home');
            } catch(e) {
                showToast("Failed to load store data. Please refresh.");
            }
        };

        // Router
        function navigate(view) {
            document.querySelectorAll('.view-section').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.nav-links a').forEach(el => el.classList.remove('active'));
            
            const target = document.getElementById('view-' + view);
            if (target) target.classList.add('active');
            
            const nav = document.getElementById('nav-' + view);
            if (nav) nav.classList.add('active');

            if(view === 'cart') renderCart();
            if(view === 'orders') renderOrders();

            window.scrollTo({ top: 0, behavior: 'smooth' });
            document.querySelector('.nav-links').classList.remove('show');
        }

        // Product Rendering
        function generateCardHTML(p) {
            const price = p.price * (1 - p.discount/100);
            const originalHTML = p.discount > 0 ? `<span class="original-price">$${p.price}</span>` : '';
            const badgeHTML = p.discount > 0 ? `<div class="badge">-${p.discount}%</div>` : '';
            
            return `
                <div class="card">
                    <div class="card-img" style="background-image: url('${p.img}')" onclick="showProductDetails(${p.id})">${badgeHTML}</div>
                    <div class="card-body">
                        <div class="category">${p.category}</div>
                        <div class="title">${p.name}</div>
                        <div style="font-size: 0.9rem; opacity: 0.8; flex-grow: 1; margin-bottom:10px;">${p.desc.substring(0, 50)}...</div>
                        <div class="price-row">
                            <div>${originalHTML}<span class="price">$${price.toFixed(2)}</span></div>
                            <div style="font-size: 0.9rem;">⭐ ${p.rating}</div>
                        </div>
                        <div class="actions">
                            <button class="btn btn-gold" onclick="addToCart(${p.id})">Add to Cart</button>
                            <button class="btn btn-icon" onclick="showProductDetails(${p.id})">👁</button>
                        </div>
                    </div>
                </div>
            `;
        }

        function renderProducts(filter = "") {
            const container = document.getElementById('products-grid');
            if(!container) return;
            container.innerHTML = STATE.products
                .filter(p => p.name.toLowerCase().includes(filter.toLowerCase()) || p.category.toLowerCase().includes(filter.toLowerCase()))
                .map(generateCardHTML).join('');
        }

        function renderFeatured() {
            const container = document.getElementById('featured-grid');
            if(container && STATE.products.length > 0) {
                container.innerHTML = STATE.products.slice(0, 4).map(generateCardHTML).join('');
            }
        }

        function showProductDetails(pid) {
            const p = STATE.products.find(x => x.id === pid);
            if(!p) return;
            const price = p.price * (1 - p.discount/100);
            showModal(`
                <div style="display:flex; gap:20px; flex-wrap:wrap;">
                    <img src="${p.img}" style="width:100%; max-width:200px; border-radius:15px; object-fit:cover;">
                    <div style="flex:1; min-width:200px;">
                        <span class="category">${p.category}</span>
                        <h2 style="margin:5px 0;">${p.name}</h2>
                        <h3 style="color:var(--coffee); margin-bottom:10px;">$${price.toFixed(2)}</h3>
                        <p style="opacity:0.8; margin-bottom:15px;">${p.desc}</p>
                        <p style="font-size:0.9rem; margin-bottom:5px;"><strong>Availability:</strong> ${p.stock}</p>
                        <button class="btn btn-gold" style="width:100%; margin-top:10px;" onclick="addToCart(${p.id})">Add to Cart</button>
                    </div>
                </div>
            `);
        }

        // Cart Logic
        async function addToCart(pid) {
            try {
                let res = await fetch('/api/cart/add', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({product_id: pid, qty: 1})
                });
                let data = await res.json();
                if(data.success) {
                    STATE.cart = data.cart;
                    updateCartCount();
                    showModal(`
                        <div style="text-align:center">
                            <h2 style="color:var(--soft-gold); margin-bottom:10px;">🛒 Added Successfully</h2>
                            <p>Item is now in your shopping bag.</p>
                            <div style="margin-top:20px; display:flex; gap:10px; justify-content:center;">
                                <button class="btn" onclick="closeModal()">Keep Shopping</button>
                                <button class="btn btn-gold" onclick="closeModal(); navigate('cart')">View Bag</button>
                            </div>
                        </div>
                    `);
                }
            } catch(e) { showToast("Error modifying cart"); }
        }

        async function updateCart(pid, action) {
            let res = await fetch('/api/cart/update', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({product_id: pid, action: action})
            });
            let data = await res.json();
            if(data.success) {
                STATE.cart = data.cart;
                updateCartCount();
                renderCart();
            }
        }

        function updateCartCount() {
            const count = Object.values(STATE.cart).reduce((a, b) => a + b, 0);
            document.getElementById('cart-count').innerText = count;
        }

        function renderCart() {
            const container = document.getElementById('cart-container');
            if(Object.keys(STATE.cart).length === 0) {
                container.innerHTML = '<div class="glass" style="padding:3rem; text-align:center; border-radius:20px;"><h3>Your bag is empty.</h3><button class="btn btn-gold" style="margin-top:20px;" onclick="navigate(\'products\')">Browse Vault</button></div>';
                return;
            }

            let html = '<div class="table-container"><table><thead><tr><th>Product</th><th>Price</th><th>Quantity</th><th>Subtotal</th></tr></thead><tbody>';
            let total = 0;

            for (const [pid, qty] of Object.entries(STATE.cart)) {
                const p = STATE.products.find(x => x.id == pid);
                if(!p) continue;
                const price = p.price * (1 - p.discount/100);
                const sub = price * qty;
                total += sub;
                html += `
                    <tr>
                        <td style="display:flex; align-items:center; gap:15px;">
                            <img src="${p.img}" width="60" style="border-radius:10px;">
                            <strong>${p.name}</strong>
                        </td>
                        <td>$${price.toFixed(2)}</td>
                        <td>
                            <div class="qty-controls">
                                <button class="qty-btn" onclick="updateCart(${p.id}, 'decrease')">-</button>
                                <span>${qty}</span>
                                <button class="qty-btn" onclick="updateCart(${p.id}, 'increase')">+</button>
                            </div>
                        </td>
                        <td><strong>$${sub.toFixed(2)}</strong></td>
                    </tr>
                `;
            }
            html += '</tbody></table></div>';
            
            const tax = total * 0.1;
            const grand = total + tax;
            html += `
                <div class="cart-summary">
                    <p style="margin-bottom:10px;">Subtotal: $${total.toFixed(2)}</p>
                    <p style="margin-bottom:10px;">Tax (10%): $${tax.toFixed(2)}</p>
                    <h2 style="color:var(--coffee); margin: 20px 0;">Total Amount: $${grand.toFixed(2)}</h2>
                    <button class="btn btn-gold" style="font-size:1.2rem; padding: 15px 40px;" onclick="processCheckout()">Secure Checkout 🔒</button>
                </div>
            `;
            container.innerHTML = html;
        }

        // Checkout Logic
        async function processCheckout() {
            showModal(`<div style="text-align:center;"><h2>Processing Payment...</h2><p style="margin-top:10px;">Securing your transaction.</p></div>`);
            try {
                let res = await fetch('/api/checkout', { method: 'POST' });
                let data = await res.json();
                
                setTimeout(() => {
                    if(data.success) {
                        STATE.cart = {};
                        STATE.orders = data.orders;
                        updateCartCount();
                        showModal(`
                            <div style="text-align:center;">
                                <h1 style="font-size:3rem; margin-bottom:10px;">🎉</h1>
                                <h2 style="color:var(--soft-gold);">Order Confirmed</h2>
                                <p style="margin: 15px 0;">Thank you for shopping at Premium Mart.</p>
                                <p><strong>Invoice ID:</strong> ${data.order_id}</p>
                                <button class="btn btn-gold" style="margin-top:20px;" onclick="closeModal(); navigate('orders')">View Orders</button>
                            </div>
                        `);
                    } else {
                        showToast("Transaction Failed");
                        closeModal();
                    }
                }, 1000);
            } catch(e) {
                showToast("Network Error");
                closeModal();
            }
        }

        // Orders Logic
        function renderOrders() {
            const container = document.getElementById('orders-container');
            if(STATE.orders.length === 0) {
                container.innerHTML = '<p>No past transactions found.</p>';
                return;
            }
            container.innerHTML = STATE.orders.map(o => `
                <div class="order-card">
                    <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--beige); padding-bottom:15px; margin-bottom:15px;">
                        <h3>Order #${o.order_id}</h3>
                        <span style="background:var(--soft-gold); color:white; padding:5px 15px; border-radius:20px; font-size:0.9rem;">${o.status}</span>
                    </div>
                    <p><strong>Date:</strong> ${o.date}</p>
                    <p><strong>Grand Total:</strong> $${o.total}</p>
                    <button class="btn" style="margin-top:15px;" onclick="showOrderDetails('${o.order_id}')">View Details</button>
                </div>
            `).join('');
        }

        function showOrderDetails(oid) {
            const o = STATE.orders.find(x => x.order_id === oid);
            if(!o) return;
            let itemsHtml = o.items.map(i => `
                <div style="display:flex; justify-content:space-between; margin-bottom:10px; padding-bottom:10px; border-bottom:1px solid #eee;">
                    <span>${i.qty}x ${i.name}</span>
                    <span>$${(i.price * i.qty).toFixed(2)}</span>
                </div>
            `).join('');

            showModal(`
                <h2>Invoice Statement</h2>
                <hr style="margin: 15px 0; border: 0; border-top: 1px solid var(--beige);">
                <p style="font-size:0.9rem; margin-bottom: 10px;"><strong>ID:</strong> ${o.order_id}</p>
                <div style="margin: 20px 0;">${itemsHtml}</div>
                <div style="text-align:right;"><h3>Total Paid: $${o.total}</h3></div>
                <button class="btn btn-gold" style="width:100%; margin-top:20px;" onclick="closeModal()">Close</button>
            `);
        }

        // Utility Modals
        function showModal(content) {
            document.getElementById('modal-body').innerHTML = content;
            const overlay = document.getElementById('modal-overlay');
            overlay.style.display = 'flex';
            setTimeout(() => overlay.style.opacity = '1', 10);
        }
        function closeModal() {
            const overlay = document.getElementById('modal-overlay');
            overlay.style.opacity = '0';
            setTimeout(() => overlay.style.display = 'none', 300);
        }
        function showToast(msg) {
            const t = document.getElementById('toast');
            t.innerText = msg;
            t.style.display = 'block';
            t.style.top = '20px';
            setTimeout(() => t.style.display = 'none', 3000);
        }
        function showLogin() {
            showModal(`
                <h2 style="text-align:center; margin-bottom:20px;">Client Login</h2>
                <div class="form-group"><input type="email" placeholder="Email Address"></div>
                <div class="form-group"><input type="password" placeholder="Password"></div>
                <button class="btn btn-gold" style="width:100%; margin-top:10px;" onclick="closeModal(); showToast('Logged in successfully!')">Sign In</button>
            `);
        }

        // Chatbot Logic
        function toggleChat() {
            const w = document.getElementById('chat-window');
            w.style.display = (w.style.display === 'none' || w.style.display === '') ? 'flex' : 'none';
        }
        async function sendChat() {
            const input = document.getElementById('chat-input');
            const msg = input.value.trim();
            if(!msg) return;

            appendMsg('user', msg);
            input.value = '';

            const loaderId = 'loader-' + Date.now();
            appendMsg('ai', '<span class="typing">...</span>', loaderId);

            try {
                let res = await fetch('/api/chat', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({message: msg})
                });
                let data = await res.json();
                document.getElementById(loaderId).innerHTML = data.response.replace(/\\n/g, '<br>').replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>');
                scrollToChatBottom();
            } catch(e) {
                document.getElementById(loaderId).innerText = "Connection lost.";
            }
        }
        function appendMsg(sender, text, id = null) {
            const box = document.getElementById('chat-messages');
            const div = document.createElement('div');
            div.className = `msg ${sender}`;
            if(id) div.id = id;
            div.innerHTML = text;
            box.appendChild(div);
            scrollToChatBottom();
        }
        function scrollToChatBottom() {
            const box = document.getElementById('chat-messages');
            box.scrollTop = box.scrollHeight;
        }
    </script>
</body>
</html>
"""

# ==========================================
# ROBUST REST API ROUTES
# ==========================================

@app.route('/')
@app.route('/<path:path>')
def serve_frontend(path=None):
    """Serve the frontend HTML."""
    print(f"🌍 Client connected to: /{path or 'home'}")
    return HTML_CONTENT

@app.route('/api/init', methods=['GET'])
def api_init():
    """Send initial store data to the frontend."""
    print("📦 Frontend requested initial store data.")
    return jsonify({
        "products": PRODUCTS,
        "cart": session.get('cart', {}),
        "orders": session.get('orders', [])
    })

@app.route('/api/cart/add', methods=['POST'])
def api_add_cart():
    try:
        data = request.json
        pid = str(data.get('product_id'))
        qty = int(data.get('qty', 1))

        cart = session.get('cart', {})
        cart[pid] = cart.get(pid, 0) + qty
        
        session['cart'] = cart
        session.modified = True  # Force Flask to save the cookie

        print(f"🛒 Added item {pid} to cart. Current Cart: {cart}")
        return jsonify({"success": True, "cart": cart})
    except Exception as e:
        print(f"❌ Error adding to cart: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/cart/update', methods=['POST'])
def api_update_cart():
    try:
        data = request.json
        pid = str(data.get('product_id'))
        action = data.get('action')
        
        cart = session.get('cart', {})
        if pid in cart:
            if action == 'increase':
                cart[pid] += 1
            elif action == 'decrease':
                if cart[pid] > 1:
                    cart[pid] -= 1
                else:
                    del cart[pid]
            elif action == 'remove':
                del cart[pid]
                
        session['cart'] = cart
        session.modified = True  # Force Flask to save the cookie
        
        print(f"🔄 Updated cart (Action: {action}). Current Cart: {cart}")
        return jsonify({"success": True, "cart": cart})
    except Exception as e:
        print(f"❌ Error updating cart: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/checkout', methods=['POST'])
def api_checkout():
    try:
        cart = session.get('cart', {})
        if not cart:
            print("⚠️ Checkout attempted with an empty cart.")
            return jsonify({"success": False, "error": "Cart is empty"}), 400
            
        total = 0
        items = []
        for str_pid, qty in cart.items():
            pid = int(str_pid)
            p = next((x for x in PRODUCTS if x['id'] == pid), None)
            if p:
                price = p['price'] * (1 - p['discount'] / 100)
                total += price * qty
                items.append({"name": p['name'], "qty": qty, "price": price})
                
        tax = total * 0.10
        grand_total = total + tax
        
        order = {
            "order_id": "PM-" + str(uuid.uuid4())[:8].upper(),
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "status": "Confirmed",
            "total": round(grand_total, 2),
            "items": items
        }
        
        orders = session.get('orders', [])
        orders.insert(0, order)
        
        # Save orders and clear cart
        session['orders'] = orders
        session['cart'] = {}
        session.modified = True  # Force Flask to save the cookie
        
        print(f"✅ Checkout successful. Order ID: {order['order_id']}")
        return jsonify({"success": True, "order_id": order['order_id'], "orders": orders})
    except Exception as e:
        print(f"❌ Checkout Error: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/chat', methods=['POST'])
def api_chat():
    user_msg = request.json.get('message', '')
    print(f"🗣️ User asked AI: {user_msg}")

    if not gemini_client:
        print("⚠️ AI Chat failed: Gemini Client is offline.")
        return jsonify({"response": "The AI is currently offline due to a missing or invalid API Key."})

    try:
        prompt = f"You are a helpful AI Concierge for an exquisite luxury store called 'Premium Mart'. Be polite and concise. User says: {user_msg}"
        response = gemini_client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        print("🤖 AI Responded successfully.")
        return jsonify({"response": response.text})
    except Exception as e:
        print(f"❌ AI Error: {e}")
        return jsonify({"response": f"AI Engine Connection Error. Details: {str(e)}"})

if __name__ == '__main__':
    # Force Flask to run cleanly
    print("\n" + "="*50)
    print("🚀 Starting Premium Mart Backend...")
    print("👉 OPEN YOUR BROWSER TO: http://127.0.0.1:5000")
    print("="*50 + "\n")
    app.run(host='127.0.0.1', port=5000, debug=True)