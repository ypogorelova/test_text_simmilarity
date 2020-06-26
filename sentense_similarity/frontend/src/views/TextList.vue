<template>
    <v-container fluid>
        <v-list class="main">
            <text-area></text-area>
            <v-divider></v-divider>
            <text-card
                v-for="text in texts.articles"
                v-bind:key="text.slug"
                v-bind:text="text"
            >
            </text-card>
        </v-list>
    </v-container>
</template>

<script>
import api from '@/api';
export default {
    data() {
        return {
            texts: []
        };
    },
    async created() {
        this.texts = await api.getArticles();
    }
};
</script>
