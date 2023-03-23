<template>
  <section class="login-main-wrapper">
    <div class="container-fluid pl-0 pr-0">
      <div class="row no-gutters">
        <div class="col-md-5 p-5 bg-white full-height">
          <div class="login-main-left">
            <div class="text-center mb-5 login-main-left-header pt-4">
              <img src="@/assets/img/favicon.png" class="img-fluid" alt="LOGO">
              <h5 class="mt-3 mb-3">Регистрация</h5>
            </div>
            <form action="#">
              <div class="form-group">
                <label>Имя</label>
                <input type="text" v-model.trim="v$.name.$model" class="form-control" placeholder="Имя">
              </div>
              <span class='error-field'
                  v-for="error in v$.name.$errors"
                  :key="error" >
                  {{ getError(`${error.$propertyPath}.${error.$validator}`) }}
                </span>
              <div class="form-group">
                <label>Telegram логин</label>
                <input type="text" v-model.trim="v$.login.$model" class="form-control" placeholder="Telegram логин">
              </div>
              <span class='error-field'
                  v-for="error in v$.login.$errors"
                  :key="error" >
                  {{ getError(`${error.$propertyPath}.${error.$validator}`) }}
                </span>
              <div class="form-group">
                <label>Пароль</label>
                <input type="password" v-model.trim="v$.password.$model" class="form-control" placeholder="Пароль">
              </div>
              <span class='error-field'
                  v-for="error in v$.password.$errors"
                  :key="error" >
                  {{ getError(`${error.$propertyPath}.${error.$validator}`) }}
                </span>
              <div class="mt-4">
                <span class='error-field'
                  v-for="error in serverErrors"
                  :key="error" >
                  {{ getError(error) }}
                </span>
                <button :disabled="v$.$invalid || isLoading" type="button" class="btn btn-outline-primary btn-block btn-lg" v-on:click="signUp">Регистрация
                </button>
              </div>
            </form>
            <div class="text-center mt-5">
              <p class="light-gray">Уже есть аккаунт? <a href="/login">Вход</a></p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import { minLength, required } from '@vuelidate/validators';
import useVuelidate from '@vuelidate/core';
import { useStore } from 'vuex';
import RegisterRequest from '@/models/RegisterRequest';
import { register } from '@/services/api-service';

@Options({
  components: {},
  validations: {
    name: {
      required,
      minLength: minLength(3),
    },
    login: {
      required,
      minLength: minLength(3),
    },
    password: {
      required,
      minLength: minLength(8),
    },
  },
})
export default class RegisterView extends Vue {
  isLoading = false;

  serverErrors: string[] = [];

  name = '';

  login = '';

  password = '';

  v$ = useVuelidate();

  store = useStore();

  errors: { [key: string]: string } = {
    'name.required': 'Обязательное поле',
    'login.required': 'Обязательное поле',
    'password.required': 'Обязательное поле',
    'name.minLength': 'Минимальная длина 3 символа',
    'login.minLength': 'Минимальная длина 3 символа',
    'password.minLength': 'Минимальная длина 8 символов',
    'user already exists': 'Пользователь уже существуе',
  };

  getError(errorKey: string): string {
    return this.errors[errorKey];
  }

  async signUp(): Promise<void> {
    const registerRequest: RegisterRequest = {
      name: this.name,
      login: this.login,
      password: this.password,
    };

    try {
      this.isLoading = true;
      this.serverErrors = [];
      const user = await register(registerRequest);
      if (user) {
        this.store.commit('setUser', user);
        this.$router.push({ name: 'home' });
      }
    } catch (ex: any) {
      if (ex) {
        this.serverErrors.push(ex.message);
      }
    } finally {
      this.isLoading = false;
    }
  }
}
</script>

<style scoped>

</style>
