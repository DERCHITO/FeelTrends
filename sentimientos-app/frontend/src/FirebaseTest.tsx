import { useEffect } from "react";
import app, { analytics } from "./firebase";

export default function FirebaseTest() {
  useEffect(() => {
    if (app) {
      // Si la app se inicializó correctamente
      console.log("Firebase conectado:", app.options.projectId);
      if (analytics) {
        console.log("Analytics habilitado");
      }
    }
  }, []);

  return (
    <div className="p-4 bg-green-100 border border-green-400 rounded">
      <h2 className="font-bold">Test de conexión a Firebase</h2>
      <p>Revisa la consola del navegador para ver el resultado.</p>
    </div>
  );
}
