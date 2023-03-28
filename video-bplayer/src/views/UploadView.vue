<template>
  <!--  <div class="container-fluid pt-5 pb-5">-->
  <!--    <div class="row">-->
  <!--      <div class="col-md-8 mx-auto text-center upload-video pt-5 pb-5">-->
  <!--        <h1><i class="fas fa-file-upload text-primary"></i></h1>-->
  <!--&lt;!&ndash;        <input class="box__file" type="file" name="file" id="file" />&ndash;&gt;-->

  <!--        <h4 class="mt-5">Выберите видео файл для загрузки</h4>-->
  <!--        <p class="land">или перетащите сюда файл</p>-->
  <!--        <div class="mt-4">-->
  <!--          <a class="btn btn-outline-primary" href="№">Загрузить</a>-->
  <!--        </div>-->
  <!--      </div>-->
  <!--    </div>-->
  <!--  </div>-->
  <div class="container-fluid upload-details">
    <div class="row">
      <div class="col-lg-12">
        <div class="main-title">
          <h6>Загрузка видео</h6>
        </div>
      </div>
    </div>
    <div class="row" v-if="progress > 0">
      <div class="col-lg-12">
        <div class="main-title">
          <h6>Детали загрузки</h6>
        </div>
      </div>
      <div class="col-lg-2">
        <div class="imgplace"></div>
      </div>
      <div class="col-lg-10">
        <div class="osahan-progress">
          <div class="progress">
            <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar"
                 v-bind:aria-valuenow="progress" aria-valuemin="0" aria-valuemax="100" :style="{ 'width': progress + '%' }"></div>
          </div>
          <div class="osahan-close">
            <a href="#"><i class="fas fa-times-circle"></i></a>
          </div>
        </div>
        <div class="osahan-desc">{{ uploadingMessage }}</div>
      </div>
    </div>
    <hr v-if="progress > 0">
    <label class="control-label">Простая загрузка файла</label>
    <input type="checkbox" v-model="isSimpleUpload" />

    <form v-if="!isSimpleUpload">
      <div class="row">
        <div class="col-sm-6">
          <div class="form-group">
            <label class="control-label">Url сервера с GPU <span class="required">*</span></label>
            <input class="form-control border-form-control" placeholder="https://localhost:5000"
                   v-model.trim="gpuServerUrl"
                   type="text">
          </div>
        </div>
      </div>

<!--      <div class="row">-->
<!--        <div class="col-sm-6">-->
<!--          <div class="form-group">-->
<!--            <label class="control-label">Url видео <span class="required">*</span></label>-->
<!--            <input class="form-control border-form-control" placeholder="https://youtube.com/anyvideo"-->
<!--                   v-model.trim="v$.url.$model"-->
<!--                   type="text">-->
<!--            <span class='error-field'-->
<!--              v-for="error in v$.url.$errors"-->
<!--              :key="error" >-->
<!--              {{ `${error.$propertyPath}.${error.$validator}` }}-->
<!--            </span>-->
<!--          </div>-->
<!--        </div>-->
<!--      </div>-->
      <div class="row">
        <div class="col-sm-6">
          <div class="form-group">
            <label class="control-label">Файл для загрузки<span class="required">*</span></label>
            <input class="box__file" ref="uploadFile" type="file" name="uploadFile" id="uploadFile" />
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-sm-6">
          <div class="form-group">
            <label class="control-label">Название <span class="required">*</span></label>
            <input class="form-control border-form-control"
                   v-model.trim="v$.name.$model"
                   placeholder="Название..."
                   type="text">
            <span class='error-field'
              v-for="error in v$.name.$errors"
              :key="error" >
              {{ getError(`${error.$propertyPath}.${error.$validator}`) }}
            </span>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-sm-6">
          <div class="form-group">
            <label class="control-label">Описание <span class="required">*</span></label>
            <input class="form-control border-form-control"
                   v-model.trim="v$.description.$model"
                   placeholder="Описание..."
                   type="text">
            <span class='error-field'
              v-for="error in v$.description.$errors"
              :key="error" >
              {{ getError(`${error.$propertyPath}.${error.$validator}`) }}
            </span>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-sm-6">
          <div class="form-group">
            <label class="control-label">Категория <span class="required">*</span></label>
            <select class="custom-select" v-model.trim="v$.category.$model">
              <option value="">Выбрать категорию</option>
              <option value="Фильмы">Фильмы</option>
              <option value="Сериалы">Сериалы</option>
              <option value="Клипы">Клипы</option>
            </select>
            <span class='error-field'
              v-for="error in v$.category.$errors"
              :key="error" >
              {{ getError(`${error.$propertyPath}.${error.$validator}`) }}
            </span>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-sm-12">
          <button :disabled="v$.$invalid" type="button" class="btn btn-success border-none" v-on:click="onSave">Загрузить и обработать</button>
        </div>
      </div>
    </form>

    <form v-if="isSimpleUpload">
      <div class="row">
        <div class="col-sm-6">
          <div class="form-group">
            <label class="control-label">Url сервера с GPU <span class="required">*</span></label>
            <input class="form-control border-form-control" placeholder="https://localhost:5000"
                   v-model.trim="gpuServerUrl"
                   type="text">
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col-sm-6">
          <div class="form-group">
            <label class="control-label">Файл для загрузки<span class="required">*</span></label>
            <input class="box__file" ref="uploadFile" type="file" name="uploadFile" id="uploadFile" />
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col-sm-6">
          <div class="form-group">
            <label class="control-label">Тип файла <span class="required">*</span></label>
            <select class="custom-select" v-model.trim="fileType">
              <option value="image">image</option>
              <option value="video">video</option>
              <option value="audio">audio</option>
            </select>
          </div>
        </div>
      </div>

      <div class="row" v-if="uploadedFileName">
        <div class="col-sm-12">
          Файл успешно загружен. Имя файла: {{ uploadedFileName }}
        </div>
      </div>

      <div class="row">
        <div class="col-sm-12">
          <button type="button" class="btn btn-success border-none" v-on:click="onSimpleUpload">Загрузить</button>
        </div>
      </div>
    </form>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import VideoDownloadRequest from '@/models/VideoDownloadRequest';
import {
  downloadVideo,
  uploadVideo,
  uploadSimpleFile,
  getVideoById,
  processStart,
  processStatus,
} from '@/services/api-service';
import useVuelidate from '@vuelidate/core';
import { minLength, required, url } from '@vuelidate/validators';
import Video from '@/models/Video';
import VideoProcessingRequest from '@/models/VideoProcessingRequest';
import Process from '@/models/Process';
import { Ref } from 'vue-property-decorator';

@Options({
  components: {},
  validations: {
    name: {
      required,
      minLength: minLength(8),
    },
    description: {
      required,
      minLength: minLength(8),
    },
    category: {
      required,
    },
  },
})
export default class UploadView extends Vue {
  uploadingMessage = '';

  progress = 0;

  v$ = useVuelidate();

  gpuServerUrl = 'http://localhost:5000';

  url = 'https://youtu.be/8TIdEezL7rc';

  name = '';

  description = '';

  category = '';

  currentVideo: Video | null = null;

  currentProcess: Process | null = null;

  currentInterval: number | null = null;

  isSimpleUpload = true;

  uploadedFileName = '';

  fileType = 'image';

  @Ref('uploadFile') readonly uploadFile!: HTMLInputElement

  errors: { [key: string]: string } = {
    'name.required': 'Обязательное поле',
    'description.required': 'Обязательное поле',
    'category.required': 'Обязательное поле',
    'name.minLength': 'Минимальная длина 6 символов',
    'description.minLength': 'Минимальная длина 8 символов',
  };

  getError(errorKey: string): string {
    return this.errors[errorKey];
  }

  async onSave() {
    // await this.downloadVideo();
    await this.uploadVideoForm();
  }

  async onSimpleUpload() {
    await this.uploadSimpleFile();
  }

  async uploadSimpleFile() {
    const { files } = this.uploadFile;
    if (!files) {
      return;
    }

    const formData = new FormData();

    // if you want to upload multiple files at once loop
    // through the array of files
    formData.append('file', files[0]);
    formData.append('type', this.fileType);

    try {
      const fileName = await uploadSimpleFile(formData);
      if (fileName) {
        this.uploadedFileName = fileName;
      }
    } catch (ex: any) {
      if (ex) {
        this.uploadingMessage = 'Ошибка попробуйте снова';
      }
    }
  }

  async uploadVideoForm() {
    const { files } = this.uploadFile;
    if (!files) {
      return;
    }

    const formData = new FormData();

    // if you want to upload multiple files at once loop
    // through the array of files
    formData.append('file', files[0]);
    formData.append('name', this.name);
    formData.append('description', this.description);
    formData.append('category', this.category);

    this.uploadingMessage = 'Загрузка видео...';
    this.progress = 10;

    try {
      // const process = await downloadVideo(videoDownloadRequest);
      const video = await uploadVideo(formData);
      if (video) {
        this.currentVideo = video;
        this.progress = 20;
        this.uploadingMessage = 'Загрузка видео завершена';
        await this.processingVideoStart();
      } else {
        this.uploadingMessage = 'Ошибка попробуйте снова';
      }
    } catch (ex: any) {
      if (ex) {
        this.uploadingMessage = 'Ошибка попробуйте снова';
      }
    }
  }

  async downloadVideo() {
    this.uploadingMessage = 'Скачивание видео...';
    this.progress = 10;
    const videoDownloadRequest: VideoDownloadRequest = {
      url: this.url,
      name: this.name,
      description: this.description,
      category: this.category,
    };

    try {
      // const process = await downloadVideo(videoDownloadRequest);
      const video = await getVideoById(5);
      if (video) {
        this.currentVideo = video;
        this.progress = 20;
        this.uploadingMessage = 'Скачивание видео завершено';
        await this.processingVideoStart();
      } else {
        this.uploadingMessage = 'Ошибка попробуйте снова';
      }
    } catch (ex: any) {
      if (ex) {
        this.uploadingMessage = 'Ошибка попробуйте снова';
      }
    }
  }

  async processingVideoStart() {
    if (this.currentVideo == null) {
      return;
    }

    this.uploadingMessage = 'Запуск обработки...';
    this.progress = 20;
    const process: Process = {
      id: 0,
      videoId: this.currentVideo.id,
      status: 0,
      dateStart: new Date(),
      dateEnd: new Date(),
      updatedAt: new Date(),
      isSuccess: false,
      errorMessage: '',
    };

    try {
      const processFromServer = await processStart(process);
      if (processFromServer) {
        this.currentProcess = processFromServer;
        this.currentInterval = setInterval(this.getAndUpdateProcessStatus, 5000);
      } else {
        this.uploadingMessage = 'Ошибка попробуйте снова';
      }
    } catch (ex: any) {
      if (ex) {
        this.uploadingMessage = 'Ошибка попробуйте снова';
      }
    }
  }

  async getAndUpdateProcessStatus() {
    if (this.currentProcess == null) {
      return;
    }

    try {
      const process = await processStatus(this.currentProcess.id);
      if (process) {
        if (process.dateEnd && process.errorMessage != null) {
          this.uploadingMessage = process.errorMessage;
          this.stopUpdate();
        }

        this.currentProcess = process;
        switch (this.currentProcess.status) {
          case 0:
            this.uploadingMessage = 'Начат процесс...';
            break;
          case 1:
            this.uploadingMessage = 'Идет процесс детектирования сцен...';
            this.progress = 30;
            break;
          case 2:
            this.uploadingMessage = 'Идет процесс преобразования Image to text...';
            this.progress = 40;
            break;
          case 3:
            this.uploadingMessage = 'Идет процесс суммаризации текстов...';
            this.progress = 60;
            break;
          case 4:
            this.uploadingMessage = 'Идет процесс перевода...';
            this.progress = 80;
            break;
          case 5:
            this.uploadingMessage = 'Идет процесс озвучивания...';
            this.progress = 90;
            break;
          case 6:
            this.uploadingMessage = 'Процесс заверщен';
            this.progress = 100;
            this.stopUpdate();
            break;
          default:
            this.uploadingMessage = 'Неизвестный статус';
        }
      } else {
        this.progress = 0;
        this.uploadingMessage = 'Ошибка попробуйте снова';
        this.stopUpdate();
      }
    } catch (ex: any) {
      if (ex) {
        this.uploadingMessage = 'Ошибка попробуйте снова';
        this.stopUpdate();
      }
    }
  }

  stopUpdate() {
    if (this.currentInterval) {
      clearInterval(this.currentInterval);
    }
  }
}
</script>
