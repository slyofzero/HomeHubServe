<template>
  <main class="d-flex flex-column gap-5">
    <div class="d-flex flex-column gap-4 p-4 border border-dark rounded">
      <h5 class="text-center fw-semibold">Looking for?</h5>
      <div class="d-flex flex-column flex-md-row justify-content-center gap-4">
        <div class="p-4 border border-dark rounded"></div>
        <div class="p-4 border border-dark rounded"></div>
        <div class="p-4 border border-dark rounded"></div>
        <div class="p-4 border border-dark rounded"></div>
      </div>
    </div>

    <div class="d-flex flex-column gap-4">
      <h5 class="fw-semibold">Service History</h5>
      <table
        class="table border-start border-end border-dark rounded overflow-hidden"
      >
        <thead class="table-dark">
          <tr>
            <th>ID</th>
            <th>Service Name</th>
            <th>Professional Name</th>
            <th>Phone No.</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td>Service 1</td>
            <td>.............</td>
            <td>.............</td>
            <td>Closed</td>
          </tr>
          <tr>
            <td>2</td>
            <td>Service 2</td>
            <td>.............</td>
            <td>.............</td>
            <td>Requested</td>
          </tr>
          <tr>
            <td>3</td>
            <td>Service 3</td>
            <td>.............</td>
            <td>.............</td>
            <td>Open</td>
          </tr>
        </tbody>
      </table>
    </div>
  </main>
</template>

<style scoped>
th,
td {
  padding: 0.5rem 1rem;
}
</style>
