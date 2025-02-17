<template>
  <Modal :show-modal="props.showModal">
    <!-- Modal Header -->
    <template #header>
      <div class="modal-header border-0">
        <h4 class="modal-title w-100 text-center">Edit Profile</h4>
        <button
          @click="closeModal"
          class="btn-close"
          aria-label="Close"
        ></button>
      </div>
    </template>

    <!-- Modal Body -->
    <template #body>
      <div class="d-flex flex-column gap-4">
        <span
          v-if="errorMessage"
          class="text-danger bg-danger-subtle rounded px-4 py-1"
          >{{ errorMessage }}</span
        >

        <p class="mb-0">
          To edit your service and years of experience you'd have to close the
          current profile and register again.
        </p>

        <div>
          <form @submit.prevent="editProfile">
            <div>
              <label for="pincode" class="form-label">Pincode</label>
              <input id="pincode" v-model="form.pincode" class="form-control" />
            </div>

            <div>
              <label for="price" class="form-label">Price</label>
              <input id="price" v-model="form.price" class="form-control" />
            </div>

            <div>
              <label for="description" class="form-label">Description</label>
              <textarea
                id="description"
                v-model="form.description"
                class="form-control shadow-none"
                rows="3"
              />
            </div>

            <!-- Modal Footer -->
            <div class="d-flex justify-content-center gap-3 mt-3">
              <button type="submit" class="btn btn-primary px-4">Edit</button>
              <button
                type="button"
                class="btn btn-secondary px-4"
                @click="closeModal"
              >
                Cancel
              </button>
            </div>
          </form>
        </div>
      </div>
    </template>
  </Modal>
</template>

<script lang="ts" setup>
import { clientFetcher, clientPut, useApi } from "@/utils/api";
import router from "@/router";
import { IApiRes, IProfessional, IService, ServiceApiRes } from "@/types";
import { ref, watch } from "vue";
import Modal from "../Modal.vue";

interface Props {
  showModal: boolean;
  professional: IProfessional;
}
const props = defineProps<Props>();

const emit = defineEmits(["close", "refreshProfessional"]);

const form = ref({
  pincode: props.professional.pincode,
  description: props.professional.description,
  price: props.professional.price,
});
const errorMessage = ref("");
const selectedService = ref<IService>();
const url = `${import.meta.env.VITE_API_URL}/service/${props.professional.service_id}` // prettier-ignore
const { data: serviceRes } = useApi<ServiceApiRes>(url);
watch(serviceRes, () => {
  selectedService.value = serviceRes.value.data.data[0];
});

// Action functions
async function closeModal() {
  emit("close");
}
async function editProfile() {
  const url = `${import.meta.env.VITE_API_URL}/professional`;
  const res = await clientPut<IApiRes>(url, form.value);

  if (form.value.price) {
    const base_price = selectedService.value.base_price;
    if (form.value.price < base_price) {
      errorMessage.value = `Price can't be lower than base price of ${selectedService.value.base_price}`;
      return;
    }
  }

  if (res.response === 200) {
    closeModal();
    errorMessage.value = "";
    router.push("/professional");
    emit("refreshProfessional");
  } else {
    errorMessage.value = res.data.message || "Couldn't update profile.";
  }
}
</script>
