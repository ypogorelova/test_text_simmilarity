<template>
    <v-container fluid>
        <v-data-table
            :headers="headers"
            :items="sentences.sentences"
            :footer-props="{ 'items-per-page-options': [10, 25, 50, 100, 200] }"
            @click:row="go"
        >
        </v-data-table>
    </v-container>
</template>

<script>
import api from '@/api';
export default {
    props: ['sentence'],

    mounted: function() {
        this.getSimilarities();
    },
    data: () => ({
        sentences: { sentences: [] },
        headers: [
            { text: 'Sentence', value: 'sentence_original', align: 'left' },
            { text: 'Score', value: 'similarity_score' },
            { text: 'Text slug', value: 'slug' }
        ]
    }),

    methods: {
        async getSimilarities() {
            this.sentences = await api.postSentenceSimilarity({
                sentence: this.sentence
            });
        },
        go(item) {
            this.$router.push({ name: 'text', params: { slug: item.slug } });
        }
    }
};
</script>
