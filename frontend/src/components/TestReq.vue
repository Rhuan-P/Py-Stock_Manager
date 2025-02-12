<!-- frontend/src/components/TesteRotas.vue -->

<template>
  <div class="max-w-md mx-auto p-4 mt-4 bg-white rounded-lg shadow-md">
    <h1 class="text-2xl font-bold mb-4">Teste Rotas</h1>
    <button
      class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
      @click="testarRotas"
    >
      Testar Rotas
    </button>
    <button
      class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded ml-2"
      @click="clearDB"
    >
      Limpar Banco de Dados
    </button>
    <ul class="list-none mb-4">
      <li v-for="rota in rotas" :key="rota.nome" class="mb-2">
        <span class="font-bold">{{ rota.nome }}:</span> {{ rota.resultado }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'TesteRotas',
  data() {
    return {
      rotas: [
        { nome: 'Criar Produto', resultado: '' },
        { nome: 'Listar Produtos', resultado: '' },
        { nome: 'Buscar Produto', resultado: '' },
        { nome: 'Adicionar Lote', resultado: '' },
        { nome: 'Atualizar Preço Lote', resultado: '' },
        { nome: 'Excluir Lote', resultado: '' },
      ],
    };
  },
  methods: {
    async testarRotas() {
      try {
        // Criar Produto
        const response1 = await axios.post('http://localhost:5000/api/produtos', {
          
          codigo: Math.floor(Math.random() * 1000)  ,
         
          nome: Math.random().toString(36).substring(2, 15) ,
        });
        this.rotas[0].resultado = response1.data.message;

        // Listar Produtos
        const response2 = await axios.get('http://localhost:5000/api/produtos');
        this.rotas[1].resultado = response2.data.length;

        // Buscar Produto
        const response3 = await axios.get('http://localhost:5000/api/produto/123');
        this.rotas[2].resultado = response3.data.nome;

        // Adicionar Lote
        const response4 = await axios.post('http://localhost:5000/api/produto/123/lote', {
          preco: Math.random() * 1000,
          quantidade: Math.floor(Math.random() * 100),
        });
        this.rotas[3].resultado = response4.data.message;

        // Atualizar Preço Lote
        const response5 = await axios.put('http://localhost:5000/api/lote/1', {
          preco: 12.99,
        });
        this.rotas[4].resultado = response5.data.message;

       // ...
       
               // Excluir Lote
               const response6 = await axios.delete('http://localhost:5000/api/lote/1');
               this.rotas[5].resultado = response6.data.message;
             } catch (error) {
               console.error(error);
             }
           },
           async clearDB() {
             try {
               const response = await axios.delete('http://localhost:5000/api/clear');
               console.log(response.data.message);
             } catch (error) {
               console.error(error);
             }
           },
         },
       };
       </script>