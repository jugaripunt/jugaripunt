import{a}from"./CCb-kr4I.js";import{_ as i,c as p,a as o,n as u,p as t,v as l,o as m}from"./mpqWqgHx.js";var b={};const f={data(){return{email:"",password:"",passwordRepeat:"",nom:"",cognoms:"",edat:""}},methods:{async submit(){var d;if(this.password!==this.passwordRepeat){alert("Les contrasenyes no coincideixen. Si us plau, intenta-ho de nou.");return}try{console.log(b.API_BASE_URL),(await a.post("jugaripunt.cat/api/jugador/",{email:this.email,contrasenya:this.password,nom:this.nom,cognoms:this.cognoms,edat:this.edat})).status===201&&(alert("Jugador registrat amb èxit!"),document.getElementById("formulariregistre").reset())}catch(e){alert(`Error de registre: ${((d=e.response)==null?void 0:d.data.error)||e.message}`)}}}},g={class:"min-h-screen flex flex-col justify-center items-center bg-cover"},x={class:"bg-white p-8 rounded-lg shadow-lg w-full max-w-md"},c={class:"mb-4"},w={class:"mb-4"},y={class:"mb-4"},v={class:"mb-4"},k={class:"mb-4"},R={class:"mb-4"};function h(d,e,E,U,r,n){return m(),p("div",g,[o("div",x,[e[14]||(e[14]=o("h1",{class:"text-3xl font-bold mb-8 text-center"}," Alta de nou usuari ",-1)),o("form",{id:"formulariregistre",onSubmit:e[6]||(e[6]=u((...s)=>n.submit&&n.submit(...s),["prevent"]))},[o("div",c,[e[7]||(e[7]=o("label",{class:"block text-gray-700",for:"email"},"Email",-1)),t(o("input",{id:"email","onUpdate:modelValue":e[0]||(e[0]=s=>r.email=s),class:"form-input mt-1 block w-full h-12 rounded px-4 border border-gray-300",type:"email",required:"",placeholder:"Email"},null,512),[[l,r.email]])]),o("div",w,[e[8]||(e[8]=o("label",{class:"block text-gray-700",for:"password"},"Contrasenya",-1)),t(o("input",{id:"password","onUpdate:modelValue":e[1]||(e[1]=s=>r.password=s),class:"form-input mt-1 block w-full h-12 rounded px-4 border border-gray-300",type:"password",required:"",placeholder:"Contrasenya"},null,512),[[l,r.password]])]),o("div",y,[e[9]||(e[9]=o("label",{class:"block text-gray-700",for:"passwordRepeat"},"Repeteix contrasenya",-1)),t(o("input",{id:"passwordRepeat","onUpdate:modelValue":e[2]||(e[2]=s=>r.passwordRepeat=s),class:"form-input mt-1 block w-full h-12 rounded px-4 border border-gray-300",type:"password",required:"",placeholder:"Repeteix contrasenya"},null,512),[[l,r.passwordRepeat]])]),o("div",v,[e[10]||(e[10]=o("label",{class:"block text-gray-700",for:"nom"},"Nom",-1)),t(o("input",{id:"nom","onUpdate:modelValue":e[3]||(e[3]=s=>r.nom=s),class:"form-input mt-1 block w-full h-12 rounded px-4 border border-gray-300",type:"text",required:"",placeholder:"Nom"},null,512),[[l,r.nom]])]),o("div",k,[e[11]||(e[11]=o("label",{class:"block text-gray-700",for:"cognoms"},"Cognoms",-1)),t(o("input",{id:"cognoms","onUpdate:modelValue":e[4]||(e[4]=s=>r.cognoms=s),class:"form-input mt-1 block w-full h-12 rounded px-4 border border-gray-300",type:"text",required:"",placeholder:"Cognoms"},null,512),[[l,r.cognoms]])]),o("div",R,[e[12]||(e[12]=o("label",{class:"block text-gray-700",for:"edat"},"Edat",-1)),t(o("input",{id:"edat","onUpdate:modelValue":e[5]||(e[5]=s=>r.edat=s),class:"form-input mt-1 block w-full h-12 rounded px-4 border border-gray-300",type:"number",required:"",placeholder:"Edat"},null,512),[[l,r.edat]])]),e[13]||(e[13]=o("button",{class:"bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-700 w-full mb-4",type:"submit"}," Registre d'usuari ",-1))],32)])])}const B=i(f,[["render",h]]);export{B as default};
