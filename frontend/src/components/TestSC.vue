<template>
  <div id="app">
    <header>
      <h1>Gestor de Estoque</h1>
      <nav>
        <router-link to="/">Página Inicial</router-link> |
        <router-link to="/add-product">Adicionar Produto</router-link>
      </nav>
    </header>

    <router-view />
  </div>
</template>

<script>
import { createApp } from 'vue';
import { createRouter, createWebHashHistory } from 'vue-router';

// Componente da lista de produtos
const ProductList = {
  template: `
    <div>
      <h2>Lista de Produtos</h2>
      <ul>
        <li v-for="product in products" :key="product.id">
          {{ product.name }} - R$ {{ product.price }}
          <router-link :to="'/product/' + product.id"> Detalhes</router-link>
        </li>
      </ul>
    </div>
  `,
  data() {
    return {
      products: [
        { id: 1, name: 'Produto A', price: '10.00' },
        { id: 2, name: 'Produto B', price: '20.00' },
      ],
    };
  },
};

// Componente de detalhes do produto
const ProductDetail = {
  template: `
    <div>
      <h2>Detalhes do Produto</h2>
      <div v-if="product">
        <p><strong>Nome:</strong> {{ product.name }}</p>
        <p><strong>Preço:</strong> R$ {{ product.price }}</p>
        <p><strong>Descrição:</strong> {{ product.description }}</p>
      </div>
      <div v-else>
        <p>Produto não encontrado.</p>
      </div>
    </div>
  `,
  data() {
    return {
      product: null,
    };
  },
  created() {
    const productId = this.$route.params.id;
    this.product = {
      id: productId,
      name: `Produto ${productId}`,
      price: '15.00',
      description: `Descrição do produto ${productId}`,
    };
  },
};

// Componente para adicionar um novo produto
const ProductForm = {
  template: `
    <div>
      <h2>Adicionar Produto</h2>
      <form @submit.prevent="submitForm">
        <input v-model="product.name" placeholder="Nome do Produto" />
        <input v-model="product.price" placeholder="Preço" />
        <button type="submit">Salvar</button>
      </form>
    </div>
  `,
  data() {
    return {
      product: {
        name: '',
        price: '',
      },
    };
  },
  methods: {
    submitForm() {
      console.log('Produto Adicionado:', this.product);
      alert('Produto adicionado!');
      this.$router.push('/');
    },
  },
};

// Definindo as rotas
const routes = [
  { path: '/', component: ProductList },
  { path: '/product/:id', component: ProductDetail },
  { path: '/add-product', component: ProductForm },
];

// Configurando o Vue Router
const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

// Componente raiz (TesteSC)
export default {
  name: 'TesteSC',
  components: {},
  router,
};
</script>

<style>
/* Estilos globais */
body {
  font-family: Arial, sans-serif;
  padding: 20px;
  background-color: #f4f4f4;
}

h2 {
  color: #333;
}

input,
button {
  padding: 8px;
  margin: 5px;
  border-radius: 4px;
}

button {
  cursor: pointer;
  background-color: #4caf50;
  color: white;
}

button:hover {
  background-color: #45a049;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  padding: 10px;
  background-color: #fff;
  margin: 5px 0;
  border-radius: 4px;
}

a {
  color: #0066cc;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

header {
  background-color: #4caf50;
  color: white;
  padding: 10px;
  text-align: center;
}

nav {
  margin-top: 10px;
}

nav a {
  color: white;
  text-decoration: none;
  margin: 0 10px;
}

nav a:hover {
  text-decoration: underline;
}
</style>
