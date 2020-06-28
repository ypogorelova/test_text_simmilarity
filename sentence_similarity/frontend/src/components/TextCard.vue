<template>
    <v-card class="mx-auto text-card">
        <v-card-subtitle>
            {{ text.body }}
        </v-card-subtitle>

        <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn icon @click="show = !show">
                <v-icon>{{
                    show ? 'mdi-chevron-up' : 'mdi-chevron-down'
                }}</v-icon>
            </v-btn>
        </v-card-actions>

        <v-expand-transition>
            <div v-show="show">
                <v-divider></v-divider>
                <v-card-text
                    class="headline font-weight-bold"
                    v-for="(sentence, index) in text.sentenceList"
                    v-bind:key="index"
                    @click="goToSimilarities(sentence)"
                >
                    {{ sentence }}
                </v-card-text>
            </div>
        </v-expand-transition>
    </v-card>
</template>

<script>
export default {
    props: ['text'],
    metaInfo() {
        return {
            title: this.text && this.text.title
        };
    },
    data() {
        return {
            show: false
        };
    },

    methods: {
        goToSimilarities(sentence) {
            this.$router.push({
                name: 'similarities',
                params: { sentence: sentence }
            });
        }
    }
};
</script>
