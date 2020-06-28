<template>
    <v-container fluid>
        <v-list class="main">
            <text-card v-bind:text="text.article"> </text-card>
        </v-list>
    </v-container>
</template>

<script>
import api from '@/api';
export default {
    props: ['slug'],
    data() {
        return {
            text: {}
        };
    },
    async created() {
        this.text = await api.getArticle(this.slug);
    },
    methods: {}
};
</script>
