import { createStore } from 'vuex';
import User from '@/models/User';

interface State {
  userId: number,
  userName: string,
}

const store = createStore<State>({
  state: {
    userId: 0,
    userName: '',
  },
  getters: {},
  mutations: {
    initialiseStore(state: State): void {
      // Check if the ID exists
      const storeInLocalStorage = localStorage.getItem('store');
      if (storeInLocalStorage) {
        // Replace the state object with the stored item
        this.replaceState(
          Object.assign(state, JSON.parse(storeInLocalStorage)),
        );
      }
    },
    setUser(state: State, payload: User): void {
      state.userId = payload.id;
      state.userName = payload.name;
    },
    clearUser(state: State): void {
      state.userId = 0;
      state.userName = '';
    },
  },
  actions: {},
  modules: {},
});

store.subscribe((mutation, state) => {
  // Store the state object as a JSON string
  localStorage.setItem('store', JSON.stringify(state));
});

export default store;
