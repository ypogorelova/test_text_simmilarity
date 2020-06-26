<template>
    <v-card flat>
        <v-form ref="form" @submit.prevent="submit">
            <v-container fluid>
                <v-row>
                    <v-col cols="12" sm="6">
                        <v-text-field
                            v-model="form.article.title"
                            :rules="rules.title"
                            color="purple darken-2"
                            label="Title"
                            required
                        ></v-text-field>
                    </v-col>
                    <v-col cols="12">
                        <v-textarea
                            v-model="form.article.body"
                            :rules="rules.body"
                            color="teal"
                        >
                            <template v-slot:label>
                                <div>Text <small>(required)</small></div>
                            </template>
                        </v-textarea>
                    </v-col>
                </v-row>
            </v-container>
            <v-card-actions>
                <v-btn text @click="resetForm">Cancel</v-btn>
                <v-spacer></v-spacer>
                <v-btn
                    text
                    :disabled="!formIsValid"
                    color="primary"
                    type="submit"
                    >Submit</v-btn
                >
            </v-card-actions>
        </v-form>
    </v-card>
</template>

<script>
import api from '@/api';
export default {
    data() {
        const defaultForm = Object.freeze({
            article: {
                title: '',
                body: ''
            }
        });

        return {
            form: Object.assign({}, defaultForm),
            rules: {
                title: [
                    val => (val || '').length > 0 || 'This field is required'
                ],
                body: [
                    val => (val || '').length > 0 || 'This field is required'
                ]
            },
            defaultForm
        };
    },

    computed: {
        formIsValid() {
            return this.form.article.title && this.form.article.body;
        }
    },

    methods: {
        resetForm() {
            this.form = Object.assign({}, this.defaultForm);
            this.$refs.form.reset();
        },
        async submit() {
            await api.createArticle(this.form);
            this.resetForm();
            await api.getArticles()
        }
    }
};
</script>
