<template>
    <div>
        <b-form-select @change="onChange" v-model="selected" :options="options"></b-form-select>
    </div>
</template>

<script>
    export default {
        name: "LabelSelector",
        props: ['sentence'],
        data() {
            return {
                selected: this.sentence.label,
                options: [
                    { value: 0, text: 'OSEF' },
                    { value: 1, text: 'Non-MANA' },
                    { value: 2, text: 'Oui-MANA' },
                ]
            }
        },
        methods: {
            onChange(value) {
                this.sentence.label = value
            },
        }
    }
</script>