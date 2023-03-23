<template>
  <router-view/>
</template>

<script lang="ts">

import { Options, Vue } from 'vue-class-component';
import User from '@/models/User';
import { useStore } from 'vuex';

@Options({
})
export default class App extends Vue {
  mounted(): void {
    const store = useStore();
    store.commit('initialiseStore');
  }
}
</script>
<style lang="scss">
</style>
