<template>
  <!-- Modal -->
  <div
    v-if="showModal"
    class="modal fade show"
    tabindex="-1"
    style="display: block"
    aria-modal="true"
    role="dialog"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content p-4">
        <!-- Modal Header -->
        <div class="modal-header border-0">
          <h4 class="modal-title w-100 text-center">Edit Service</h4>
          <button
            @click="closeModal"
            class="btn-close"
            aria-label="Close"
          ></button>
        </div>

        <!-- Modal Body -->
        <div class="modal-body">
          <form @submit.prevent="(e: Event) => e.preventDefault()">
            <!-- Service Name -->
            <div class="mb-3">
              <label for="serviceName" class="form-label">
                <strong>Service Name:</strong>
              </label>
              <input
                type="text"
                id="serviceName"
                class="form-control"
                v-model="formData.name"
                placeholder="Enter service name"
                required
              />
            </div>

            <!-- Description -->
            <div class="mb-3">
              <label for="description" class="form-label">
                <strong>Description:</strong>
              </label>
              <textarea
                id="description"
                class="form-control"
                v-model="formData.description"
                placeholder="Enter description"
                rows="3"
                required
              ></textarea>
            </div>

            <!-- Base Price -->
            <div class="mb-3">
              <label for="basePrice" class="form-label">
                <strong>Base Price:</strong>
              </label>
              <input
                type="number"
                id="basePrice"
                class="form-control"
                v-model="formData.price"
                placeholder="Enter base price"
                required
              />
            </div>

            <!-- Modal Footer -->
            <div class="d-flex justify-content-center gap-3">
              <button
                type="submit"
                @click="addModal"
                class="btn btn-primary px-4"
              >
                Update
              </button>
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
    </div>
  </div>

  <!-- Custom Backdrop -->
  <div
    v-if="showModal"
    style="
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.5);
      z-index: 1040;
    "
  ></div>
</template>

<script lang="ts" setup>
import { ref, watch } from "vue";
import router from "@/router";
import { IApiRes, ServiceApiRes } from "@/types";
import { clientPut, useApi } from "@/utils/api";

const props = defineProps({
  showModal: {
    type: Boolean,
    required: true,
  },
  service: {
    type: [Number, null],
    required: true,
  },
});

const emit = defineEmits(["close", "refreshServices"]);

const formData = ref({
  name: "",
  description: "",
  price: "",
});
const errorMessage = ref("");

const url = `${import.meta.env.VITE_API_URL}/service/${props.service}`;
const { data: serviceData } = useApi<ServiceApiRes>(url);

function closeModal() {
  emit("close");
}
async function addModal() {
  const url = `${import.meta.env.VITE_API_URL}/service/${props.service}`;
  const res = await clientPut<IApiRes>(url, formData.value);
  if (res.response === 200) {
    closeModal();
    errorMessage.value = "";
    router.push("/admin");
    emit("refreshServices");
  } else {
    errorMessage.value = res.data.message || "Couldn't create a new service";
  }
}

watch(serviceData, (newData) => {
  if (newData) {
    const serviceData = newData?.data.data[0];
    if (serviceData) {
      formData.value.name = serviceData.name;
      formData.value.description = serviceData.description;
      formData.value.price = String(serviceData.price);
    }
  }
});
</script>
