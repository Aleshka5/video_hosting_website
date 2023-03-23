<template>
  <div class="container-fluid pt-5 pb-5">
    <div class="row">
      <div class="col-md-8 mx-auto text-center upload-video pt-5 pb-5">
        <h1><i class="fas fa-file-upload text-primary"></i></h1>
<!--        <input class="box__file" type="file" name="file" id="file" />-->

        <h4 class="mt-5">Выберите видео файл для загрузки</h4>
        <p class="land">или перетащите сюда файл</p>
        <div class="mt-4">
          <a class="btn btn-outline-primary" href="№">Загрузить</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';

@Options({
  components: {},
})
export default class UploadView extends Vue {
}
</script>
