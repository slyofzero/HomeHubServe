<template>
  <div
    class="container p-4 p-md-5 rounded border border-dark d-flex flex-column gap-4"
  >
    <h2>Register as a Professional</h2>
    <span
      v-if="errorMessage"
      class="text-danger bg-danger-subtle rounded px-4 py-1"
      >{{ errorMessage }}</span
    >
    <form
      class="d-flex flex-column gap-4"
      @submit.prevent="registerProfessional"
    >
      <div>
        <label for="name" class="form-label">Experience in years</label>
        <input
          type="text"
          id="experience"
          v-model="form.experience"
          class="form-control"
          required
        />
      </div>
      <div>
        <label for="service_id" class="form-label">Service</label>
        <select
          id="service_id"
          class="form-select mb-2"
          aria-label="Default select example"
          v-model="form.service_id"
          required
        >
          <option value="">Select a service</option>
          <option
            v-for="(service, index) in services"
            :key="index"
            :value="service.id"
          >
            {{ service.name }} (Rs {{ service.price }})
          </option>
        </select>
      </div>
      <div>
        <label for="description" class="form-label">Description</label>
        <textarea
          id="description"
          v-model="form.description"
          class="form-control"
          rows="3"
          required
        ></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Register</button>
    </form>
  </div>
</template>

<script lang="ts" setup>
import { ref, watch } from "vue";
import router from "@/router";
import { IApiRes, IService, ServiceApiRes } from "@/types";
import { clientPoster, useApi } from "@/utils/api";
import { useUserStore } from "@/stores";
import { JWT_KEY_NAME } from "@/utils/constants";

// Check if user is logged in or allowed
const userStore = useUserStore();
if (!userStore.isLoggedIn && !localStorage.getItem(JWT_KEY_NAME))
  router.push("/login");

watch(userStore, () => {
  if (!userStore.isLoggedIn) router.push("/login");
});

const services = ref<IService[]>([]);
const form = ref({
  experience: "",
  service_id: "",
  description: "",
});
const errorMessage = ref("");

// Set services
const servicesUrl = `${import.meta.env.VITE_API_URL}/service`;
const { data: serviceRes } = useApi<ServiceApiRes>(servicesUrl);

watch(serviceRes, () => {
  const new_services = serviceRes.value?.data.data;
  services.value = new_services ? new_services : [];
});

// Register professional
async function registerProfessional() {
  const url = `${import.meta.env.VITE_API_URL}/professional`;

  try {
    const res = await clientPoster<IApiRes>(url, form.value);

    if (res.response >= 400) {
      errorMessage.value =
        res.data.message || "Invalid input. Please try again.";
    } else {
      errorMessage.value = "";
      userStore.setUserRole("REG_PROFESSIONAL");
      router.push("/professional");
    }
  } catch (error) {
    errorMessage.value = "An unexpected error occurred. Please try again.";
    console.error("Error during login:", error);
  }
}
</script>

<style scoped>
.container {
  max-width: 600px;
}
</style>
